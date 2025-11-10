from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from tools.visit_website import visit_website
from tools.notion_tool import save_to_notion

load_dotenv()

model = ChatOllama(
    model="llama3.1:8b", 
    temperature=0
)

search = DuckDuckGoSearchResults()
memory = MemorySaver()
tools = [search, visit_website, save_to_notion]

agent = create_react_agent(
    model, 
    tools, 
    checkpointer=memory
    )

config = {"configurable": {"thread_id": "123abc"}}


        
def call_agent(query: str):
    response = agent.invoke({"messages": HumanMessage(content=query)}, config)

    
    for message in response["messages"]:
        print(f"\n=========={message.type}===========")
        print(message.content, "\n")

        # Eğer message bir tool çağrısı içeriyorsa
        if hasattr(message, "tool_calls") and message.tool_calls:
            for call in message.tool_calls:
                print("==========tool_call===========")
                print(f"Tool Name: {call.get('name')}")
                print(f"Args: {call.get('args')}")
                print(f"Type: {call.get('type')}\n")

        
        if hasattr(message, "metadata") and message.metadata:
            print("Metadata:", message.metadata, "\n")

    
    answer = response["messages"][-1].content

    title_prompt = f"Generate a short and descriptive title (max 6 words) for this question:\n\n{query}"
    title_response = model.invoke([HumanMessage(content=title_prompt)])
    title = title_response.content.strip().replace('"', '')
    
    notion_result = save_to_notion.func(title=title, query=query, answer=answer)
    print("==========notion_result===========")
    print(notion_result, "\n")

    return answer



        
        
    