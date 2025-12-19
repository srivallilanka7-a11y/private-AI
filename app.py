import streamlit as st
from assistant import ask_ai

st.set_page_config(page_title="Personal AI", layout="centered")
st.title("🔐 My Personal AI Assistant (Offline)")

user_input = st.text_input("You:")
if user_input:
    with st.spinner("AI is thinking..."):
        reply = ask_ai(user_input)
    st.text_area("AI:", reply, height=200, key="ai_output")


