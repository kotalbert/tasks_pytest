import pytest
from src import tasks


def test_add_raises():
    """add() should raise exception with wrong type param."""
    with pytest.raises(TypeError):
        tasks.add(task='not a Task object')


def test_start_db_raises():
    """start_task_db() should raise exceptin with wrong db type."""
    with pytest.raises(ValueError) as excinfo:
        tasks.start_task_db('some/path', 'mysql')
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "db_type must be a 'tiny' or 'mongo'"


def test_get_raises():
    """ get() should raise an exception with wrong type param. """
    with pytest.raises(TypeError):
        tasks.get(task_id='123')
