from src.tasks.app import Task
from src.tasks.api import add, get


def test_add_return_valid_id():
    """ tasks.add(<valid task>) should return an integer."""
    new_task = Task('do something')
    task_id = add(new_task)
    assert isinstance(task_id, int)


def test_added_task_has_id_set():
    """ task_id field should be set by task_add()"""
    new_task = Task('sit in chair', owner='me', done=True)
    task_id = add(new_task)

    task_from_db = get(task_id)

    assert task_from_db.id == task_id
