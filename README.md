# DevTrack CLI — Python Project Management Tool

DevTrack CLI is an object-oriented, interactive terminal application built in Python for managing projects, tracking tasks, and handling role-based user authentication using persistent local JSON storage.

## Features

* **Object-Oriented Architecture:** Uses inheritance (`Person` -> `User`, `Entity` base model), encapsulation (role & task status properties), and object serialization.
* **Authentication System:** Secure registration and login flows with SHA-256 password hashing.
* **Role-Based Access Control (RBAC):** Restricts administrative features to `Admin` users while giving `User` roles standard permissions.
* **Project & Task Management:** Create projects, track due dates, and dynamically assign tasks to specific projects.
* **Persistent Data Storage:** Saves data cleanly to local JSON files with full serialization support.

---

## Project Structure

```text
cli-project-manager/
├── data/
│   ├── users.json
│   └── projects.json
├── models/
│   ├── base.py
│   ├── user.py
│   ├── project.py
│   └── task.py
├── utils/
│   ├── auth.py
│   ├── decorators.py
│   └── storage.py
├── tests/
│   ├── test_auth.py
│   └── test_models.py
├── main.py
├── README.md
└── requirements.txt