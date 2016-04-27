"""Add Event.is_hidden

Revision ID: 45778f751d09
Revises: ac151f9f2237
Create Date: 2016-04-27 19:01:48.192665

"""
from alembic import op
from sqlalchemy import Column
from sqlalchemy import Boolean


# revision identifiers, used by Alembic.
revision = '45778f751d09'
down_revision = 'ac151f9f2237'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table("events") as batch_op:
        batch_op.add_column(Column('is_hidden', Boolean, default=False))


def downgrade():
    pass
