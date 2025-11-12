import os
from agents.email_agent import send_email
from agents.browser_agent import search_web
from agents.weather_agent import get_weather
from agents.task_agent import add_task, complete_task, get_tasks, get_xp
from agents.schedule_agent import schedule_meeting


def process_command(command):
    command = command.lower().strip()

    # ----- EMAIL -----
    if "email" in command or "send mail" in command:
        try:
            return send_email("receiver@example.com", "Hello!", "This is a test email from Present OS.")
        except Exception as e:
            return f"📧 Email sending failed: {e}"

    # ----- SEARCH -----
    elif "search" in command or "browse" in command:
        query = command.replace("search", "").replace("browse", "").strip()
        if not query:
            return "❌ Please specify what to search. Example: 'search latest AI trends'"
        try:
            results = search_web(query)
            return results if results else "❌ No results found."
        except Exception as e:
            return f"🌐 Web search failed: {e}"

    # ----- WEATHER -----
    elif "weather" in command or "temperature" in command:
        city = command.replace("weather", "").replace("update", "").strip()
        if not city:
            return "🌍 Please specify a city. Example: 'weather update Mumbai'"
        try:
            return get_weather(city)
        except Exception as e:
            return f"🌦 Weather check failed: {e}"

    # ----- ADD TASK -----
    elif "add task" in command:
        parts = command.replace("add task", "").strip().split(" at ")
        task_name = parts[0].strip()
        time_str = parts[1].strip() if len(parts) > 1 else "09:00"
        if not task_name:
            return "📝 Please provide a task name. Example: 'add task gym at 7:00'"
        return add_task(task_name, time_str)

    # ----- COMPLETE TASK -----
    elif "complete" in command:
        task = command.replace("complete", "").strip()
        if not task:
            return "✅ Please specify which task to complete. Example: 'complete gym'"
        return complete_task(task)

    # ----- VIEW TASKS -----
    elif "view tasks" in command or "show tasks" in command or "tasks" in command:
        return get_tasks()

    # ----- SCHEDULE MEETING -----
    elif "schedule" in command and "meeting" in command:
        return schedule_meeting("Team Meeting", "2025-11-12 16:00")

    # ----- XP -----
    elif "xp" in command or "points" in command:
        return get_xp()

    # ----- UNKNOWN -----
    else:
        return (
            "🤔 Sorry, I didn’t understand that.\n\n"
            "Try commands like:\n"
            "📧 'send email'\n"
            "🌤 'weather update Mumbai'\n"
            "🕒 'add task go gym at 6:00'\n"
            "✅ 'complete gym'\n"
            "📋 'show tasks'\n"
            "🏆 'show xp'\n"
        )
