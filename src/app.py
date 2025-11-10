import streamlit as st
from agent import call_agent

st.title("AI Agent")

with st.sidebar:
    st.header("Setting")
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

# Chat geçmişini session_state'de sakla
if "messages" not in st.session_state:
    st.session_state.messages = []

# Eski mesajları göster
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Yeni mesaj
if query := st.chat_input("Ask me anything!"):
    # Kullanıcı mesajını ekle ve göster
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.write(query)
    
    # Agent'tan cevap al
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = call_agent(query)
            st.write(response)
    
    # Asistan mesajını ekle
    st.session_state.messages.append({"role": "assistant", "content": response})