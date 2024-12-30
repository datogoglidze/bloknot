import os
from dataclasses import dataclass
from pathlib import Path
from typing import Self

from alembic import command
from alembic.config import Config


@dataclass
class Alembic:
    config: Config

    @classmethod
    def from_env(cls, script_location: Path) -> Self:
        dsn = os.environ["DSN"]

        config = Config()
        config.set_main_option("sqlalchemy.url", f"sqlite:///{dsn}")
        config.set_main_option("script_location", str(script_location))

        return cls(config)

    def upgrade(self, revision: str = "head") -> None:
        command.upgrade(self.config, revision)


def migrate_db() -> None:
    if "DSN" in os.environ:
        source = Path(__file__).resolve().parent.parent.parent.joinpath("migrations")
        Alembic.from_env(source).upgrade()
