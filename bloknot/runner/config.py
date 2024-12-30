from __future__ import annotations

from dataclasses import dataclass, field

from fastapi import FastAPI

from apexdevkit.environment import value_of_env
from apexdevkit.fastapi import (
    FastApiBuilder,
    RestfulServiceBuilder,
)
from apexdevkit.fastapi.dependable import DependableBuilder
from apexdevkit.fastapi.name import RestfulName
from apexdevkit.fastapi.router import RestfulRouter

from bloknot.infra.rest.notes import NoteFields, RestfulNoteBuilder
from bloknot.runner.factory import InMemory, Sqlite


@dataclass
class BloknotApi:
    routes: dict[str, RestfulRouter] = field(default_factory=dict)
    infra: InMemory | Sqlite = field(init=False)

    def with_infra(self, value: InMemory | Sqlite) -> BloknotApi:
        self.infra = value

        return self.with_notes(RestfulNoteBuilder(value))

    def with_notes(self, builder: RestfulServiceBuilder) -> BloknotApi:
        self.routes["notes"] = (
            RestfulRouter()
            .with_name(RestfulName("note"))
            .with_fields(NoteFields())
            .with_create_one_endpoint(
                dependency=DependableBuilder().from_infra(builder)
            )
            .with_delete_one_endpoint(
                dependency=DependableBuilder().from_infra(builder)
            )
            .with_read_all_endpoint(dependency=DependableBuilder().from_infra(builder))
            .with_read_one_endpoint(dependency=DependableBuilder().from_infra(builder))
        )

        return self

    def build(self) -> FastAPI:
        api = (
            FastApiBuilder()
            .with_title("WMS")
            .with_description("Apex warehouse management system")
            .with_version(value_of_env(variable="RELEASE", default="unknown"))
            .with_route(**{name: route.build() for name, route in self.routes.items()})
            .build()
        )

        return api
