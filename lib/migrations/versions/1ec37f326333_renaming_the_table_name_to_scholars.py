"""Renaming the table name to scholars

Revision ID: 1ec37f326333
Revises: 1f3a42a88998
Create Date: 2024-12-14 17:25:18.560818

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1ec37f326333'
down_revision: Union[str, None] = '1f3a42a88998'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')