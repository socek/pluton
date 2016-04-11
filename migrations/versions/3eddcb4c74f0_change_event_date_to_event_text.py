"""Change Event.date to Event.text

Revision ID: 3eddcb4c74f0
Revises: fb398eeaeffe
Create Date: 2016-04-11 20:34:34.019857

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = '3eddcb4c74f0'
down_revision = 'fb398eeaeffe'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('events', 'data', new_column_name='raw')


def downgrade():
    pass
