import argparse
from models.project import Project
from models.task import Task
from utils.auth import register_user, authenticate_user
from utils.storage import load_projects, save_projects, load_users
from utils.decorators import require_auth, require_admin

def handle_register(args):
    user = register_user(args.name, args.email, args.password, args.role)
    if user:
        print(f"Registered user: {user.name} ({user.role})")
    else:
        print("Error: Email already exists.")

@require_auth
def handle_create_project(user, args):
    projects = load_projects()
    new_project = Project(title=args.title, description=args.description, owner_email=user.email, due_date=args.due_date)
    projects.append(new_project)
    save_projects(projects)
    print(f"Project created! ID: {new_project.id}")

def handle_list_projects(args):
    projects = load_projects()
    if not projects:
        print("No projects found.")
        return
    
    print(f"{'ID':<10} {'Title':<20} {'Owner':<25} {'Due Date':<12} {'Tasks':<5}")
    print("-" * 75)
    for p in projects:
        print(f"{p.id:<10} {p.title:<20} {p.owner_email:<25} {p.due_date:<12} {len(p.tasks):<5}")

@require_auth
def handle_add_task(user, args):
    projects = load_projects()
    target = next((p for p in projects if p.id == args.project_id), None)
    if not target:
        print(f"Error: Project {args.project_id} not found.")
        return
    
    task = Task(title=args.title, assigned_to=args.assigned_to or user.email)
    target.add_task(task)
    save_projects(projects)
    print(f"Task '{task.title}' added to Project {target.id}")

@require_admin
def handle_list_users(user, args):
    users = load_users()
    print(f"{'ID':<10} {'Name':<15} {'Email':<25} {'Role':<10}")
    print("-" * 65)
    for u in users:
        print(f"{u.id:<10} {u.name:<15} {u.email:<25} {u.role:<10}")

def main():
    parser = argparse.ArgumentParser(description="CLI Project Manager")
    subparsers = parser.add_subparsers(dest="command")

    # Register
    reg = subparsers.add_parser("register")
    reg.add_argument("--name", required=True)
    reg.add_argument("--email", required=True)
    reg.add_argument("--password", required=True)
    reg.add_argument("--role", choices=["User", "Admin"], default="User")

    # Create Project
    cp = subparsers.add_parser("create-project")
    cp.add_argument("--email", required=True)
    cp.add_argument("--password", required=True)
    cp.add_argument("--title", required=True)
    cp.add_argument("--description", default="")
    cp.add_argument("--due-date", default="N/A")

    # List Projects
    subparsers.add_parser("list-projects")

    # Add Task
    at = subparsers.add_parser("add-task")
    at.add_argument("--email", required=True)
    at.add_argument("--password", required=True)
    at.add_argument("--project-id", required=True)
    at.add_argument("--title", required=True)
    at.add_argument("--assigned-to", default="")

    # List Users
    lu = subparsers.add_parser("list-users")
    lu.add_argument("--email", required=True)
    lu.add_argument("--password", required=True)

    args = parser.parse_args()

    if args.command == "register":
        handle_register(args)
    elif args.command == "list-projects":
        handle_list_projects(args)
    elif args.command in ["create-project", "add-task", "list-users"]:
        session_user = authenticate_user(args.email, args.password)
        if args.command == "create-project":
            handle_create_project(session_user, args)
        elif args.command == "add-task":
            handle_add_task(session_user, args)
        elif args.command == "list-users":
            handle_list_users(session_user, args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()