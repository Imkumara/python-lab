from models.base import Entity

class Task(Entity):
    """Task entity managed inside Projects."""
    def __init__(self, title: str, status: str = "Pending", assigned_to: str = "Unassigned", **kwargs):
        super().__init__(**kwargs)
        self.title = title
        self._status = status
        self.assigned_to = assigned_to

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, new_status: str):
        valid = ["Pending", "In Progress", "Completed"]
        if new_status not in valid:
            raise ValueError(f"Status must be one of {valid}")
        self._status = new_status

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status,
            "assigned_to": self.assigned_to,
            "created_at": self.created_at
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            entity_id=data["id"],
            title=data["title"],
            status=data["status"],
            assigned_to=data["assigned_to"],
            created_at=data.get("created_at")
        )