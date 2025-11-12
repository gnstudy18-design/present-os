import streamlit as st
from agents.ai_agent import process_command
from agents.task_agent import view_tasks

# Safe import for Voice Agent
try:
    from agents.voice_agent import listen_command
    VOICE_AVAILABLE = True
except Exception as e:
    VOICE_AVAILABLE = False
    st.warning("🎤 Voice input unavailable on this platform. Falling back to text mode.")

st.set_page_config(page_title="Present OS", layout="wide")
st.title("🧠 Present OS — AI Multi-Agent System")

# Mode selection
mode = st.radio("Choose Input Mode:", ["Text", "Voice"])

if mode == "Text" or not VOICE_AVAILABLE:
    command = st.text_input("Type your command:")
elif mode == "Voice":
    if st.button("🎙 Speak"):
        try:
            command = listen_command()
            st.write(f"You said: {command}")
        except Exception as e:
            st.error("Voice input failed. Please type instead.")
            command = ""
    else:
        command = ""

if command:
    st.info("Processing your command...")
    response = process_command(command)
    st.success(response)

st.divider()
st.header("📋 Your Tasks")
st.dataframe(view_tasks())
