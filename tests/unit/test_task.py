"""Test the Task data type."""

from src.tasks import Task


def test_asdict():
    """`_asdict()` should return a dictionary."""

    t_task = Task('do something', 'okken', True, 21)
    t_dict = t_task._asdict()
    expected = {
        'summary': 'do something',
        'owner': 'okken',
        'done': True,
        'id': 21
    }
    assert t_dict == expected


def test_replace():
    """`replace()` should change passed in fields."""
    t_before = Task('finish book', 'brian', False, 10)
    t_after = t_before._replace(id=10, done=True)
    t_expected = Task('finish book', 'brian', True, 10)
    assert t_after == t_expected


def test_defaults():
    """Using no parameters should invoke defaults."""
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2


def test_member_access():
    """Test .field functionality of namedtuple."""
    t = Task('buy milk', 'Brian')
    assert t.owner == 'Brian'
    assert (t.done, t.id) == (False, None)