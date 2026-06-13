from pydantic import BaseModel, ValidationError
class Task(BaseModel):
    title: str
    priority: str = "low"
    completed: bool = False
class TaskNotFoundError(Exception):
    pass
tasks = {}
next_id = 1
def get_all_tasks() -> list:
    return list(tasks.values())
def get_task(id: int) -> dict:
    if id not in tasks:
        raise TaskNotFoundError("Task not found")
    return tasks[id]
def create_task(data: dict) -> dict:
    global next_id
    task = Task(**data)
    task_data = {
        "id": next_id,
        "title": task.title,
        "priority": task.priority,
        "completed": task.completed
    }
    tasks[next_id] = task_data
    next_id += 1
    return task_data
def update_task(id: int, data: dict) -> dict:
    if id not in tasks:
        raise TaskNotFoundError("Task not found")
    task = Task(**data)
    tasks[id] = {
        "id": id,
        "title": task.title,
        "priority": task.priority,
        "completed": task.completed
    }
    return tasks[id]
def delete_task(id: int) -> bool:
    if id not in tasks:
        raise TaskNotFoundError("Task not found")
    del tasks[id]
    return True
while True:
    print("\n1. Create Task")
    print("2. View All Tasks")
    print("3. View One Task")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Exit")
    choice = input("Enter choice: ")
    try:
        if choice == "1":
            title = input("Title: ")
            priority = input("Priority: ")
            task = create_task({
                "title": title,
                "priority": priority
            })
            print("Task Created")
            print(task)
        elif choice == "2":
            print(get_all_tasks())
        elif choice == "3":
            id = int(input("Enter ID: "))
            print(get_task(id))
        elif choice == "4":
            id = int(input("Enter ID: "))
            title = input("New Title: ")
            priority = input("New Priority: ")
            print(
                update_task(
                    id,
                    {
                        "title": title,
                        "priority": priority
                    }
                )
            )
        elif choice == "5":
            id = int(input("Enter ID: "))
            delete_task(id)
            print("Task Deleted")
        elif choice == "6":
            print("Goodbye")
            break
        else:
            print("Invalid Choice")
    except TaskNotFoundError as e:
        print(e)
    except ValidationError as e:
        print("Validation Error")
        print(e)