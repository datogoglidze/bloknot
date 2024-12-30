import os

from dotenv import load_dotenv
from typer import Typer, echo

from apexdevkit.server import UvicornServer

from bloknot.runner.config import BloknotApi
from bloknot.runner.factory import InMemory, Sqlite

cli = Typer(
    no_args_is_help=True,
    add_completion=False,
)


@cli.command()
def run(host: str = "0.0.0.0", port: int = 8000, root_path: str = "") -> None:
    load_dotenv()

    (
        UvicornServer.from_env()
        .with_host(host)
        .and_port(port)
        .on_path(root_path)
        .run(BloknotApi().with_infra(infra_factory()).build())
    )


def infra_factory() -> InMemory | Sqlite:
    if "DSN" not in os.environ:
        echo("Using in-memory storage...")
        return InMemory()

    echo("Using Sqlite storage...")
    return Sqlite()
