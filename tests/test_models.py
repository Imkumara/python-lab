import pytest  # type: ignore
from models.user import User
from models.project import Project
from models.task import Task

def test_user_inheritance_and_properties():
    user = User(name="Alice", email="alice@test.com", password_hash="hashed_secret", role="User")
    assert user.name == "Alice"
    assert user.role == "User"
    
    with pytest.raises(ValueError):
        user.role = "Superuser"  # Invalid role check

def test_project_task_relationship():
    project = Project(title="CLI Tool", description="Build Python CLI", owner_email="lead@dev.com")
    task = Task(title="Setup JSON Storage")
    project.add_task(task)

    assert len(project.tasks) == 1
    assert project.tasks[0].title == "Setup JSON Storage"

def test_task_status_encapsulation():
    task = Task(title="Write Unit Tests")
    assert task.status == "Pending"
    
    task.status = "Completed"
    assert task.status == "Completed"

    with pytest.raises(ValueError):
        task.status = "InvalidStatus"