import datetime

class Task:
    def __init__(self, title, deadline):
        self.title = title
        self.deadline = deadline
        self.completed = False
        self.completion_date = None

    def mark_as_completed(self, completion_date):
        self.completed = True
        self.completion_date = completion_date

class DailyPlanner:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def edit_task(self, task_number, new_title, new_deadline):
        task_index = task_number - 1
        if task_index < len(self.tasks):
            task = self.tasks[task_index]
            task.title = new_title
            task.deadline = new_deadline
            print("Task edited successfully.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        task_index = task_number - 1
        if task_index < len(self.tasks):
            del self.tasks[task_index]
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")

    def show_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks found.")
        else:
            for i, task in enumerate(self.tasks):
                status = "Completed" if task.completed else "Not Completed"
                print(f"{i+1}) {task.title} | Deadline: {task.deadline} | Status: {status}")
                if task.completed:
                    print(f"  Completion Date: {task.completion_date}")

# Function to handle user input and interact with the DailyPlanner
def main():
    planner = DailyPlanner()
    
    while True:
        print("\n===== Daily Planner =====")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. Show Tasks")
        print("5. Mark Task as Completed")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            deadline = input("Enter task deadline (YYYY-MM-DD): ")
            deadline = datetime.datetime.strptime(deadline, "%Y-%m-%d")
            task = Task(title, deadline)
            planner.add_task(task)
            print("Task added successfully.")
        elif choice == "2":
            planner.show_tasks()
            task_number = int(input("Enter task number to edit: "))
            new_title = input("Enter new task title: ")
            new_deadline = input("Enter new task deadline (YYYY-MM-DD): ")
            new_deadline = datetime.datetime.strptime(new_deadline, "%Y-%m-%d")
            planner.edit_task(task_number, new_title, new_deadline)
        elif choice == "3":
            planner.show_tasks()
            task_number = int(input("Enter task number to delete: "))
            planner.delete_task(task_number)
        elif choice == "4":
            planner.show_tasks()
        elif choice == "5":
            planner.show_tasks()
            task_number = int(input("Enter task number to mark as completed: "))
            completion_date = input("Enter completion date (YYYY-MM-DD): ")
            completion_date = datetime.datetime.strptime(completion_date, "%Y-%m-%d")
            planner.tasks[task_number - 1].mark_as_completed(completion_date)
            print("Task marked as completed.")
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
