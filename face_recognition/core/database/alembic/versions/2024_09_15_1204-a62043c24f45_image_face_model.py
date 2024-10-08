"""image_face model

Revision ID: a62043c24f45
Revises: ff61d185c5c8
Create Date: 2024-09-15 12:04:57.744336

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a62043c24f45"
down_revision: Union[str, None] = "ff61d185c5c8"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "image_faces",
        sa.Column("age", sa.DECIMAL(precision=4, scale=1), nullable=False),
        sa.Column(
            "gender", sa.Enum("MALE", "FEMALE", name="gender_enum"), nullable=False
        ),
        sa.Column("image_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["image_id"],
            ["task_images.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("image_faces")
