import streamlit as st
from agents.ai_agent import process_command
from agents.task_agent import get_tasks, get_xp

# ---------------------------
# 🌈 Page Configuration
# ---------------------------
st.set_page_config(
    page_title="AI Task Assistant",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------
# 🎨 Custom Styling
# ---------------------------
st.markdown("""
    <style>
    .main {
        background-color: #eef1f7;
        color: #1e1e1e;
        font-family: 'Segoe UI', sans-serif;
    }
    .task-card {
        background-color: #ffffff;
        border-left: 6px solid #007bff;
        color: #000;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .xp-badge {
        background: linear-gradient(90deg, #4facfe 0%, #00f2fe 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        font-size: 22px;
    }
    </style>
""", unsafe_allow_html=True)


# ---------------------------
# 🧠 Header
# ---------------------------
st.markdown("<h1 class='header-title'>🤖 AI Task Assistant</h1>", unsafe_allow_html=True)
st.write("Your personal productivity companion — manage your tasks, earn XP, and stay organized!")

st.divider()

# ---------------------------
# 🗣️ Command Input Section
# ---------------------------
st.subheader("💬 Type your command:")
command = st.text_input("Try: `add task workout at 07:30`, `complete workout`, `view tasks`, or `xp`")

if command:
    with st.spinner("Processing your command..."):
        try:
            response = process_command(command)
            st.success(response)
        except Exception as e:
            st.error(f"❌ Error: {e}")

st.divider()

# ---------------------------
# 📋 Dashboard Layout
# ---------------------------
col1, col2 = st.columns([1.5, 1])

with col1:
    st.subheader("📅 Scheduled Tasks")
    tasks_output = get_tasks()
    if "No tasks" in tasks_output:
        st.info("No tasks scheduled yet. Try adding one!")
    else:
        # Display formatted tasks
        for line in tasks_output.split("\n")[1:]:
            status_icon = "✅" if "Done" in line else "🕒"
            st.markdown(f"<div class='task-card'>{status_icon} {line}</div>", unsafe_allow_html=True)

with col2:
    st.subheader("🏆 Progress Tracker")
    xp_output = get_xp()
    st.markdown(f"<div class='xp-badge'>{xp_output}</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 💡 Command Examples:")
    st.markdown("""
    - ➕ `add task morning walk at 06:30`  
    - ✅ `complete morning walk`  
    - 📋 `view tasks`  
    - 🏆 `xp`
    """)

st.markdown("---")
st.caption("🚀 Powered by Multi-Agent AI — built with Streamlit & Python")
