from models.base import Entity

class Person(Entity):
    """Base Person class establishing inheritance."""
    def __init__(self, name: str, email: str, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email

class User(Person):
    """User entity supporting Role-Based Access Control (RBAC)."""
    def __init__(self, name: str, email: str, password_hash: str, role: str = "User", **kwargs):
        super().__init__(name=name, email=email, **kwargs)
        self.password_hash = password_hash
        self._role = role  # Encapsulated role attribute

    @property
    def role(self) -> str:
        return self._role

    @role.setter
    def role(self, new_role: str):
        if new_role not in ["Admin", "User"]:
            raise ValueError("Invalid role type.")
        self._role = new_role

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password_hash": self.password_hash,
            "role": self.role,
            "created_at": self.created_at
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            entity_id=data["id"],
            name=data["name"],
            email=data["email"],
            password_hash=data["password_hash"],
            role=data.get("role", "User"),
            created_at=data.get("created_at")
        )