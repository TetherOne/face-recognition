"""task model

Revision ID: c1f4ce4defab
Revises:
Create Date: 2024-09-14 23:58:37.898819

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c1f4ce4defab"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "tasks",
        sa.Column("faces", sa.Integer(), nullable=True),
        sa.Column("men", sa.Integer(), nullable=True),
        sa.Column("women", sa.Integer(), nullable=True),
        sa.Column("average_male_age", sa.DECIMAL(precision=4, scale=1), nullable=True),
        sa.Column(
            "average_female_age", sa.DECIMAL(precision=4, scale=1), nullable=True
        ),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.CheckConstraint("average_female_age >= 0"),
        sa.CheckConstraint("average_male_age >= 0"),
        sa.CheckConstraint("faces >= 0"),
        sa.CheckConstraint("men >= 0"),
        sa.CheckConstraint("women >= 0"),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("tasks")
