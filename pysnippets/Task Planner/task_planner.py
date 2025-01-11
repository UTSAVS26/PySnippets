import time
from threading import Timer

# Task Manager Class
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name, priority, duration):
        self.tasks.append({"task": task_name, "priority": priority, "duration": duration})
        print(f"Task '{task_name}' added with priority {priority} and reminder set for {duration} seconds.")
        self._set_reminder(task_name, duration)

    def view_tasks(self):
        if not self.tasks:
            print("No tasks added yet!")
            return
        sorted_tasks = sorted(self.tasks, key=lambda x: x['priority'])
        print("\nYour Tasks:")
        for i, task in enumerate(sorted_tasks, 1):
            print(f"{i}. {task['task']} (Priority: {task['priority']}, Reminder in: {task['duration']} seconds)")

    def _set_reminder(self, task_name, duration):
        def reminder():
            print(f"\n[Reminder] Time to complete your task: {task_name}!")
        Timer(duration, reminder).start()

# Main Program
if __name__ == "__main__":
    manager = TaskManager()
    while True:
        print("\nDaily Task Planner")
        print("1. Add a Task")
        print("2. View Tasks")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task name: ")
            priority = int(input("Enter priority (1 = High, 2 = Medium, 3 = Low): "))
            duration = int(input("Enter reminder duration in seconds: "))
            manager.add_task(task, priority, duration)
        elif choice == "2":
            manager.view_tasks()
        elif choice == "3":
            print("Goodbye! Stay productive!")
            break
        else:
            print("Invalid choice. Please try again!")
