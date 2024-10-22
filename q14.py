import pickle
import os

class TaskManager:
    def __init__(self, filename='tasks.pkl'):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from the pickle file."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'rb') as file:
                    self.tasks = pickle.load(file)
            except (pickle.PickleError, EOFError) as e:
                print("Error loading tasks:", e)
                self.tasks = []  
    def save_tasks(self):
        """Save tasks to the pickle file."""
        with open(self.filename, 'wb') as file:
            pickle.dump(self.tasks, file)

    def add_task(self, task):
        """Add a new task to the list."""
        self.tasks.append(task)
        self.save_tasks()
        print(f'Task added: "{task}"')

    def remove_task(self, task):
        """Remove a task from the list."""
        try:
            self.tasks.remove(task)
            self.save_tasks()
            print(f'Task removed: "{task}"')
        except ValueError:
            print(f'Task "{task}" not found in the list.')

    def show_tasks(self):
        """Display all tasks."""
        if self.tasks:
            print("Your tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("No tasks found.")

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Management System")
        print("1. Add task")
        print("2. Remove task")
        print("3. Show tasks")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            task = input("Enter the task: ")
            task_manager.add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            task_manager.remove_task(task)
        elif choice == '3':
            task_manager.show_tasks()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

main()
