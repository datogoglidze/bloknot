import time
from dataclasses import dataclass, field
from uuid import uuid4


@dataclass(frozen=True)
class Note:
    content: str
    title: str | None = None
    date: str = field(default_factory=lambda: str(int(time.time())))

    id: str = field(default_factory=lambda: str(uuid4()))
