"""add_audit_columns_to_usuarios

Revision ID: a1b2c3d4e5f6
Revises: 3635a4326110
Create Date: 2026-04-09 18:32:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'a1b2c3d4e5f6'
down_revision: Union[str, None] = '3635a4326110'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('usuarios', sa.Column('fecha_creacion', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False))
    op.add_column('usuarios', sa.Column('fecha_edicion', sa.DateTime(timezone=True), nullable=True))


def downgrade() -> None:
    op.drop_column('usuarios', 'fecha_edicion')
    op.drop_column('usuarios', 'fecha_creacion')
