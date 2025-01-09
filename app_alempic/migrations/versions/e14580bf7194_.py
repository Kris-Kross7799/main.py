"""empty message

Revision ID: e14580bf7194
Revises: c6db6a43c1ab
Create Date: 2025-01-09 13:35:11.894067

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e14580bf7194'
down_revision: Union[str, None] = 'c6db6a43c1ab'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
