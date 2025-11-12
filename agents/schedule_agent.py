# agents/schedule_agent.py

import datetime

meetings = []

def schedule_meeting(title, date_time_str):
    """Schedule a meeting and store it in memory."""
    try:
        meeting_time = datetime.datetime.strptime(date_time_str, "%Y-%m-%d %H:%M")
        meetings.append({"title": title, "time": meeting_time})
        return f"📅 Meeting '{title}' scheduled for {meeting_time.strftime('%b %d, %Y at %I:%M %p')}"
    except ValueError:
        return "⚠️ Invalid date format. Please use YYYY-MM-DD HH:MM format."

def view_meetings():
    """Return all scheduled meetings."""
    if not meetings:
        return "No meetings scheduled yet."
    return "\n".join(
        [f"{m['title']} — {m['time'].strftime('%b %d, %Y %I:%M %p')}" for m in meetings]
    )
