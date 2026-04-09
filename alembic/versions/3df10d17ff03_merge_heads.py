"""merge_heads

Revision ID: 3df10d17ff03
Revises: e1bb86702a2b, a1b2c3d4e5f6
Create Date: 2026-04-09 18:34:18.354786

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '3df10d17ff03'
down_revision: Union[str, None] = ('e1bb86702a2b', 'a1b2c3d4e5f6')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
