"""empty message

Revision ID: 1b883f30d6fc
Revises: e14580bf7194
Create Date: 2025-01-09 14:01:06.541030

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1b883f30d6fc'
down_revision: Union[str, None] = 'e14580bf7194'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
