from langchain_core.tools import tool
from notion_client import Client
import os

@tool
def save_to_notion(title: str, query: str, answer: str) -> str:
    """Save information to Notion database.
    
    Args:
        title: Title of the entry
        query: The user's question
        answer: Content/answer to save
    
    Returns:
        Success or error message
    """
    try:
        notion = Client(auth=os.getenv("NOTION_API_KEY"))
        database_id = os.getenv("NOTION_DATABASE_ID")
        
        notion.pages.create(
            parent={"database_id": database_id},
            properties={
                "Title": {
                    "title": [{"text": {"content": title[:100]}}]
                },
                "Query": {
                    "rich_text": [{"text": {"content": query[:2000]}}]
                },
                "Answer": {
                    "rich_text": [{"text": {"content": answer[:2000]}}]
                }
            }
        )
        
        return f"✅ Successfully saved to Notion!"
    
    except Exception as e:
        return f"❌ Error: {str(e)}"