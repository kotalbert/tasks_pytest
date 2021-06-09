from typing import Any, Optional


class Task:
    def __init__(self, summary: Optional[str] = None, owner: Optional[str] = None, done: Optional[bool] = False,
                 task_id: Optional[int] = None):
        self.summary = summary
        self.owner = owner
        self.done = done
        self.id = task_id

    def _asdict(self):
        return self.__dict__

    def _replace(self, **kwargs):
        self.__dict__.update(kwargs)
        return self

    def __eq__(self, other: Any):
        return (self.summary == other.summary) & \
               (self.owner == other.owner) \
               & (self.done == other.done) \
               & (self.id == other.id)
