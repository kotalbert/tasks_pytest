from typing import Any, List

from src.tasks.app import Task

"""
def​ add(task):  ​# type: (Task) -> int​
def​ get(task_id):  ​# type: (int) -> Task​
def​ list_tasks(owner=None):  ​# type: (str|None) -> list of Task​
def​ count():  ​# type: (None) -> int​
def​ update(task_id, task):  ​# type: (int, Task) -> None​
def​ delete(task_id):  ​# type: (int) -> None​
def​ delete_all():  ​# type: () -> None​
def​ unique_id():  ​# type: () -> int​
def​ start_tasks_db(db_path, db_type):  ​# type: (str, str) -> None​
def​ stop_tasks_db():  ​# type: () -> None​
"""


def add(task: Any) -> int:
    if not isinstance(task, Task):
        raise TypeError
    return -1


def start_task_db(db_path: str, db_type: str) -> None:
    db_types = ('tiny', 'mongo')
    if db_type not in db_types:
        raise ValueError("db_type must be a 'tiny' or 'mongo'")


def get(task_id: int) -> Task:
    if not isinstance(task_id, int):
        raise TypeError


def list_tasks(owner: str) -> List[Task]:
    if not isinstance(owner, str):
        raise TypeError
    return []
