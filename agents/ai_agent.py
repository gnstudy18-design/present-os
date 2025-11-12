from agents.email_agent import send_email
from agents.browser_agent import search_web
from agents.weather_agent import get_weather
from agents.task_agent import add_task, complete_task, get_xp
from agents.schedule_agent import schedule_meeting

def process_command(command):
    command = command.lower()

    if "email" in command or "send" in command:
        return send_email("receiver@example.com", "Hello!", "This is a test email from Present OS.")
    
    elif "search" in command or "browse" in command:
        query = command.replace("search", "").replace("browse", "").strip()
        return search_web(query)
    
    elif "weather" in command:
        city = command.replace("weather", "").strip() or "New York"
        return get_weather(city)
    
    elif "add task" in command:
        task = command.replace("add task", "").strip()
        return add_task(task)
    
    elif "complete" in command:
        task = command.replace("complete", "").strip()
        return complete_task(task)
    
    elif "schedule" in command:
        return schedule_meeting("Meeting", "2025-11-12 16:00")
    
    elif "xp" in command:
        xp = get_xp()
        return f"🏆 You have {xp} XP!"
    
    else:
        return "🤔 Sorry, I didn’t understand that. Try: 'send email', 'check weather', or 'search Python'."
