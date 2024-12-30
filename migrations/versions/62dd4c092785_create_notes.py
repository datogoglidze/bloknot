"""create notes

Revision ID: 62dd4c092785
Revises:
Create Date: 2024-12-30 17:27:59.771473

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "62dd4c092785"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
            CREATE TABLE IF NOT EXISTS NOTES(
                id          TEXT    NOT NULL    PRIMARY KEY,
                date        TEXT    NOT NULL,
                content     TEXT    NOT NULL,
                title       TEXT
            );
        """
    )


def downgrade() -> None:
    pass
