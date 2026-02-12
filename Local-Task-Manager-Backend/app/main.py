import asyncio
from .task_service import TaskService

task_service = TaskService()

async def main():
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            title = input("Task title: ")
            await task_service.add_task(title)

        elif choice == "2":
            tasks = task_service.list_tasks()
            for t in tasks:
                print(f'{t["id"]}: {t["title"]} [{t["status"]}]')

        elif choice == "3":
            tid = int(input("Task id: "))
            task_service.complete_task(tid)

        elif choice == "4":
            tid = int(input("Task id: "))
            task_service.delete_task(tid)

        elif choice == "5":
            break

asyncio.run(main())
