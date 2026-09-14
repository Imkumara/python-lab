import uuid
from datetime import datetime

class Entity:
    """Base class providing common attributes."""
    def __init__(self, entity_id=None, created_at=None):
        self._id = entity_id or str(uuid.uuid4())[:8]
        self._created_at = created_at or datetime.now().isoformat()

    @property
    def id(self):
        return self._id

    @property
    def created_at(self):
        return self._created_at