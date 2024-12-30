from __future__ import annotations

from dataclasses import dataclass
from functools import cache
from typing import Any

from apexdevkit.environment import environment_variable
from apexdevkit.repository import (
    InMemoryByteStore,
    KeyValueStore,
)
from apexdevkit.repository.connector import SqliteFileConnector, SqliteInMemoryConnector


@dataclass(frozen=True)
class Sqlite:
    dsn: str = environment_variable("DSN", default="")

    @property
    def connector(self) -> SqliteInMemoryConnector | SqliteFileConnector:
        return SqliteFileConnector(self.dsn) if self.dsn else SqliteInMemoryConnector()


@dataclass(frozen=True)
class InMemory:
    @cache
    def store_for(self, resource: str) -> KeyValueStore[Any]:
        return InMemoryByteStore()
