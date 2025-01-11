# Daily Task Planner with Priority and Reminder

A lightweight Python-based **Daily Task Planner** designed to help you organize your day effectively. Add tasks with priorities, set reminders, and view tasks sorted by their importance. This snippet is a simple yet powerful tool to enhance productivity and time management in your daily life.

---

## Features
### 1. Add Tasks
- Create tasks with:
  - **Task Name**: A description of the task.
  - **Priority Levels**:
    - `1` = High Priority  
    - `2` = Medium Priority  
    - `3` = Low Priority  
  - **Reminder Duration**: Set a timer (in seconds) to get a reminder.

### 2. View Tasks
- Display all tasks sorted by priority, showing:
  - Task name
  - Priority level
  - Time left for reminders (if any)

### 3. Task Reminder
- Notifies you when it’s time to complete a task using a **reminder system** powered by Python’s `Timer` class.

---

## Usage
### Interactive Options
1. **Run the Script**:
   ```bash
   python task_planner.py
   ```
2. Follow the menu options:
   - Add tasks with their priority and reminder duration.
   - View the list of tasks sorted by priority.
   - Exit the program when done.

### Example Interaction:
```text
Daily Task Planner
1. Add a Task
2. View Tasks
3. Exit
Enter your choice: 1

Enter task name: Morning Workout
Enter priority (1 = High, 2 = Medium, 3 = Low): 1
Enter reminder duration in seconds: 10
Task 'Morning Workout' added with priority 1 and reminder set for 10 seconds.

[Reminder] Time to complete your task: Morning Workout!
```

---

## Code Overview
### Main Components:
1. **TaskManager Class**:
   - Handles task management, sorting, and reminders.
2. **Interactive Menu**:
   - Provides a user-friendly interface to interact with the planner.

### How the Reminder Works:
- Uses Python's `Timer` class to schedule a notification for each task after the specified duration.

---

## Potential Enhancements
- Save tasks to a file (e.g., JSON or CSV) to retain them between sessions.
- Add functionality to delete completed tasks.
- GUI support for enhanced usability.
- Integration with external APIs like Google Calendar or Slack for advanced notifications.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Acknowledgments
- This project uses Python's built-in threading module (`Timer`) for reminders.
- Inspired by the need for lightweight productivity tools.

Stay productive and organized!
