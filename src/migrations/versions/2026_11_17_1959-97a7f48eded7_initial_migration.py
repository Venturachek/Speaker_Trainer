"""Initial migration

Revision ID: 97a7f48eded7
Revises:
Create Date: 2026-11-17 19:59:32.874829

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "97a7f48eded7"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "topics",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column(
            "theme",
            sa.Enum(
                "SPACE",
                "HISTORY",
                "BIOLOGY",
                "TECHNOLOGY",
                "PHYSICS",
                "GEOGRAPHY",
                "PSYCHOLOGY",
                "MEDICINE",
                "ECONOMICS",
                "ART",
                name="themes",
            ),
            nullable=False,
        ),
        sa.Column("description", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )

def downgrade() -> None:
    op.drop_table("topics")