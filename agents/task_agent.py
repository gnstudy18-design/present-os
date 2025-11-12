import schedule
import time
import threading
from datetime import datetime
from agents.email_agent import send_email  # optional email reminders

# In-memory store
user_xp = 0
tasks = []


def add_task(task_name, time_str="09:00"):
    """Add and schedule a new task."""
    try:
        schedule.every().day.at(time_str).do(run_task, task_name=task_name)
        tasks.append({"task": task_name, "time": time_str, "done": False})
        return f"✅ Task '{task_name}' scheduled for {time_str}."
    except Exception as e:
        return f"❌ Failed to schedule task: {e}"


def run_task(task_name):
    """Execute a scheduled task and award XP."""
    global user_xp
    user_xp += 10
    print(f"⏰ Running task: {task_name} — +10 XP!")

    for t in tasks:
        if t["task"].lower() == task_name.lower():
            t["done"] = True

    # Optional email reminder
    try:
        send_email("your_email@example.com", "Task Reminder", f"Your task '{task_name}' is running now.")
    except Exception as e:
        print(f"📧 Email reminder failed: {e}")


def complete_task(task_name):
    """Mark a task as completed and give XP."""
    global user_xp
    for t in tasks:
        if t["task"].lower() == task_name.lower() and not t["done"]:
            t["done"] = True
            user_xp += 10
            return f"🎯 Task '{task_name}' marked complete! +10 XP"
    return f"⚠️ Task '{task_name}' not found or already done."


def get_tasks():
    """Return formatted list of tasks."""
    if not tasks:
        return "📋 No tasks scheduled."
    lines = ["📅 Your Tasks:"]
    for t in tasks:
        status = "✅ Done" if t["done"] else "🕒 Pending"
        lines.append(f"- {t['task']} at {t['time']} ({status})")
    return "\n".join(lines)


def get_xp():
    """Show total XP."""
    return f"🏆 Your XP: {user_xp}"


def run_scheduler():
    """Continuously run the scheduler in background."""
    while True:
        schedule.run_pending()
        time.sleep(1)


# Start scheduler in a daemon thread
threading.Thread(target=run_scheduler, daemon=True).start()
