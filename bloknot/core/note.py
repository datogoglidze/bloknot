from dataclasses import dataclass, field
from uuid import uuid4


@dataclass(frozen=True)
class Note:
    date: str
    content: str
    title: str | None = None

    id: str = field(default_factory=lambda: str(uuid4()))
