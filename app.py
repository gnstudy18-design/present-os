import streamlit as st
from agents.ai_agent import process_command
from agents.voice_agent import listen_command
from agents.task_agent import view_tasks

st.set_page_config(page_title="Present OS", layout="wide")
st.title("🧠 Present OS — AI Multi-Agent System")

mode = st.radio("Choose Input Mode:", ["Text", "Voice"])
if mode == "Text":
    command = st.text_input("Type your command:")
elif mode == "Voice":
    if st.button("🎙 Speak"):
        command = listen_command()
        st.write(f"You said: {command}")
    else:
        command = ""

if command:
    st.info("Processing your command...")
    response = process_command(command)
    st.success(response)

st.divider()
st.header("📋 Your Tasks")
st.dataframe(view_tasks())
