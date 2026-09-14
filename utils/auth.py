import hashlib
from typing import Optional
from models.user import User
from utils.storage import load_users, save_users

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(name: str, email: str, password: str, role: str = "User") -> Optional[User]:
    users = load_users()
    if any(u.email == email for u in users):
        return None
    new_user = User(name=name, email=email, password_hash=hash_password(password), role=role)
    users.append(new_user)
    save_users(users)
    return new_user

def authenticate_user(email: str, password: str) -> Optional[User]:
    users = load_users()
    hashed = hash_password(password)
    for u in users:
        if u.email == email and u.password_hash == hashed:
            return u
    return None