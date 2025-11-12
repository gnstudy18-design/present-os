# agents/task_agent.py

tasks = []
xp_points = 0

def add_task(task_name):
    """Add a new task and award XP."""
    global xp_points
    tasks.append({"task": task_name, "status": "pending"})
    xp_points += 10
    return f"✅ Task '{task_name}' added! (+10 XP)"

def complete_task(task_name):
    """Mark a task complete and award XP."""
    global xp_points
    for task in tasks:
        if task["task"].lower() == task_name.lower() and task["status"] == "pending":
            task["status"] = "completed"
            xp_points += 20
            return f"🎉 Task '{task_name}' completed! (+20 XP)"
    return f"⚠️ No pending task found with the name '{task_name}'."

def get_xp():
    """Return total XP earned."""
    return xp_points

def view_tasks():
    """Return list of all tasks."""
    return tasks
