from __future__ import annotations

from dataclasses import dataclass
from functools import cache
from typing import Any

from apexdevkit.environment import environment_variable
from apexdevkit.formatter import DataclassFormatter
from apexdevkit.repository import (
    Database,
    InMemoryByteStore,
    InMemoryRepository,
    KeyValueStore,
    Repository,
)
from apexdevkit.repository.connector import SqliteFileConnector, SqliteInMemoryConnector
from apexdevkit.repository.sql import SqlFieldBuilder
from apexdevkit.repository.sqlite import SqliteRepository, SqliteTableBuilder

from bloknot.core.note import Note


@dataclass(frozen=True)
class Sqlite:
    dsn: str = environment_variable("DSN", default="")

    @property
    def connector(self) -> SqliteInMemoryConnector | SqliteFileConnector:
        return SqliteFileConnector(self.dsn) if self.dsn else SqliteInMemoryConnector()

    def notes(self) -> Repository[Note]:
        return SqliteRepository(
            db=Database(self.connector),
            table=SqliteTableBuilder[Note]()
            .with_name("NOTES")
            .with_fields(
                [
                    SqlFieldBuilder().with_name("id").as_id().build(),
                    SqlFieldBuilder().with_name("date").build(),
                    SqlFieldBuilder().with_name("content").build(),
                    SqlFieldBuilder().with_name("title").build(),
                ]
            )
            .with_formatter(DataclassFormatter(Note))
            .build(),
        )


@dataclass(frozen=True)
class InMemory:
    @cache
    def store_for(self, resource: str) -> KeyValueStore[Any]:
        return InMemoryByteStore()

    def notes(self) -> Repository[Note]:
        return InMemoryRepository[Note]().with_store(self.store_for("notes")).build()
