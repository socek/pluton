"""Rename client_id to endpoint_id

Revision ID: c8c1daae3ec3
Revises: a1d83bc371bb
Create Date: 2016-05-01 13:42:08.635303

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = 'c8c1daae3ec3'
down_revision = 'a1d83bc371bb'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table("reaction_links") as batch_op:
        batch_op.alter_column('client_id', new_column_name='endpoint_id')
    with op.batch_alter_table("events") as batch_op:
        batch_op.alter_column('client_id', new_column_name='endpoint_id')


def downgrade():
    pass
