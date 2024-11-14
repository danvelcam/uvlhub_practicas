"""[bot]merging heads

Revision ID: 7f0b47e635e9
Revises: 0ba9654475a5, eb62cdc96051
Create Date: 2024-11-14 17:07:22.242400

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f0b47e635e9'
down_revision = ('0ba9654475a5', 'eb62cdc96051')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
