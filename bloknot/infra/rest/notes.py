from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from apexdevkit.fastapi import RestfulRepository, RestfulServiceBuilder
from apexdevkit.fastapi.schema import SchemaFields
from apexdevkit.fastapi.service import RestfulService
from apexdevkit.formatter import DataclassFormatter
from apexdevkit.http import JsonDict
from apexdevkit.repository import Repository

from bloknot.core.note import Note


class NoteFields(SchemaFields):
    def readable(self) -> JsonDict:
        return (
            JsonDict()
            .with_a(id=str)
            .and_a(date=str)
            .and_a(content=str)
            .and_a(title=str | None)
        )

    def writable(self) -> JsonDict:
        return self.readable().drop("id").drop("date")


@dataclass
class RestfulNoteBuilder(RestfulServiceBuilder):
    infra: _Infra

    def build(self) -> RestfulService:
        return RestfulRepository(
            repository=self.infra.notes(),
            formatter=DataclassFormatter(Note),
        )


class _Infra(Protocol):
    def notes(self) -> Repository[Note]:
        pass
