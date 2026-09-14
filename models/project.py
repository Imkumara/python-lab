from typing import List
from models.base import Entity
from models.task import Task

class Project(Entity):
    """Project entity containing a 1-to-many relationship with Tasks."""
    def __init__(self, title: str, description: str, owner_email: str, due_date: str = "N/A", tasks: List[Task] = None, **kwargs):
        super().__init__(**kwargs)
        self.title = title
        self.description = description
        self.owner_email = owner_email
        self.due_date = due_date
        self.tasks: List[Task] = tasks if tasks is not None else []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "owner_email": self.owner_email,
            "due_date": self.due_date,
            "created_at": self.created_at,
            "tasks": [task.to_dict() for task in self.tasks]
        }

    @classmethod
    def from_dict(cls, data: dict):
        tasks = [Task.from_dict(t) for t in data.get("tasks", [])]
        return cls(
            entity_id=data["id"],
            title=data["title"],
            description=data["description"],
            owner_email=data["owner_email"],
            due_date=data.get("due_date", "N/A"),
            created_at=data.get("created_at"),
            tasks=tasks
        )