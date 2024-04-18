"""Initial migration

Revision ID: e4b4df7ab80d
Revises: 5ce97a753a10
Create Date: 2024-04-17 20:44:45.735198

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e4b4df7ab80d'
down_revision: Union[str, None] = '5ce97a753a10'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('temperature', sa.Column('date_time', sa.DateTime(), nullable=False))
    op.drop_column('temperature', 'datetime')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('temperature', sa.Column('datetime', sa.DATETIME(), nullable=False))
    op.drop_column('temperature', 'date_time')
    # ### end Alembic commands ###
