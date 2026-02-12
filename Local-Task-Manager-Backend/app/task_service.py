from datetime import datetime
import asyncio
from .file_service import FileService
from .config import DATA_FILE
from .logger import logger

class Task:
    def __init__(self, id, title, status="pending"):
        self.id = id
        self.title = title
        self.status = status
        self.created_at = datetime.now().isoformat()

    def to_dict(self):
        return self.__dict__

    def __str__(self):
        return f"[{self.id}] {self.title} ({self.status})"


class TaskService:
    def __init__(self):
        self.file_service = FileService(DATA_FILE)

    def _load_tasks(self):
        return self.file_service.read_json()

    async def add_task(self, title):
        tasks = self._load_tasks()
        task_id = len(tasks) + 1

        task = Task(task_id, title)
        tasks.append(task.to_dict())

        await asyncio.sleep(0.2)  # simulate async
        self.file_service.write_json(tasks)

        logger.info(f"Task added: {title}")

    def list_tasks(self):
        tasks = self._load_tasks()
        return tasks

    def complete_task(self, task_id):
        tasks = self._load_tasks()

        for t in tasks:
            if t["id"] == task_id:
                t["status"] = "done"
                logger.info(f"Task completed: {task_id}")
                break

        self.file_service.write_json(tasks)

    def delete_task(self, task_id):
        tasks = self._load_tasks()
        tasks = [t for t in tasks if t["id"] != task_id]

        self.file_service.write_json(tasks)
        logger.info(f"Task deleted: {task_id}")
