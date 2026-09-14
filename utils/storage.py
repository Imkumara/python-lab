import json
import os
from typing import List
from models.user import User
from models.project import Project

DATA_DIR = os.path.join(os.path.dirname(__file__), "../data")
USERS_FILE = os.path.join(DATA_DIR, "users.json")
PROJECTS_FILE = os.path.join(DATA_DIR, "projects.json")

def _ensure_dir():
    os.makedirs(DATA_DIR, exist_ok=True)
    for filepath in [USERS_FILE, PROJECTS_FILE]:
        if not os.path.exists(filepath):
            with open(filepath, "w") as f:
                json.dump([], f)

def load_users() -> List[User]:
    _ensure_dir()
    try:
        with open(USERS_FILE, "r") as f:
            data = json.load(f)
            return [User.from_dict(u) for u in data]
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_users(users: List[User]):
    _ensure_dir()
    with open(USERS_FILE, "w") as f:
        json.dump([u.to_dict() for u in users], f, indent=4)

def load_projects() -> List[Project]:
    _ensure_dir()
    try:
        with open(PROJECTS_FILE, "r") as f:
            data = json.load(f)
            return [Project.from_dict(p) for p in data]
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_projects(projects: List[Project]):
    _ensure_dir()
    with open(PROJECTS_FILE, "w") as f:
        json.dump([p.to_dict() for p in projects], f, indent=4)