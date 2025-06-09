# Notebook RWN

A simple command-line task manager in Python to add, mark, delete, and list your tasks, with persistent storage in a JSON file.

## Features

- Add new tasks
- Mark tasks as completed
- Delete tasks
- List all tasks
- Tasks are saved in `taches.json` for persistence

## Project Structure

```
.
├── addTask.py
├── deleteTask.py
├── main.py
├── markedTask.py
├── save.py
├── taches.json
├── __pycache__/
└── .gitignore
```

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-folder>
    ```

2. (Optional) Create a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

### Usage

Run the main program:

```sh
python main.py
```

Follow the on-screen menu to manage your tasks.

### Data Persistence

- All tasks are stored in `taches.json`.
- The file is automatically created and updated as you use the application.

## File Descriptions

- [`main.py`](main.py): Entry point and main menu logic.
- [`addTask.py`](addTask.py): Functionality to add new tasks.
- [`deleteTask.py`](deleteTask.py): Functionality to delete tasks.
- [`markedTask.py`](markedTask.py): Functionality to mark tasks as completed.
- [`save.py`](save.py): Handles saving tasks to `taches.json`.
- [`taches.json`](taches.json): Stores your tasks (auto-generated).
- [`__pycache__/`](__pycache__): Python bytecode cache (ignored by git).
- [`.gitignore`](.gitignore): Files and folders ignored by git.

## Example

```
***BIENVENUE DANS LE NOTEBOOK RWN***
***CHOISSISEZ UNE OPTION***

1. Afficher les taches
2. Ajouter une tache
3. Marquer une tache comme terminée
4. Supprimer une tache
5. Quitter
```

## License

MIT License

---

*Generated with [gitdocify](https://github.com/gitdocify/gitdocify) style.*
