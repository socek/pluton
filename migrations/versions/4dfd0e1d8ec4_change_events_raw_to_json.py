"""Change Events.raw to json.

Revision ID: 4dfd0e1d8ec4
Revises: 3eddcb4c74f0
Create Date: 2016-04-17 20:51:15.158286

"""
from alembic import op
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import JSON

# revision identifiers, used by Alembic.
revision = '4dfd0e1d8ec4'
down_revision = '3eddcb4c74f0'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table("events") as batch_op:
        batch_op.drop_column('raw')
        batch_op.add_column(Column('raw', JSON))


def downgrade():
    pass
