import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage

# --- Gemini API Setup ---
GOOGLE_API_KEY = "AIzaSyDxsw9J-iEMveIeydO9o3qaJKZoT6VJaZ4"

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=GOOGLE_API_KEY,
)

# --- Streamlit UI Setup ---
st.set_page_config(page_title="🌟 Gemini Chatbot", page_icon="🤖")
st.title("🤖 Gemini AI Chatbot")
st.markdown("Ask anything... Powered by **Gemini 1.5 Flash**")

# --- Initialize Session State ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- User Input ---
user_input = st.chat_input("Type your message here...")

# --- Display Chat History ---
for msg in st.session_state.chat_history:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

# --- Handle User Input ---
if user_input:
    # Show user message
    st.chat_message("user").write(user_input)
    human_msg = HumanMessage(content=user_input)
    st.session_state.chat_history.append(human_msg)

    # Get response from Gemini
    with st.chat_message("assistant"):
        with st.spinner("Gemini is thinking..."):
            ai_msg = llm.invoke(st.session_state.chat_history)
            st.write(ai_msg.content)
            st.session_state.chat_history.append(ai_msg)
