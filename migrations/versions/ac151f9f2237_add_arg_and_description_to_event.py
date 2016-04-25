"""add arg and description to Event

Revision ID: ac151f9f2237
Revises: f04372fa8f80
Create Date: 2016-04-25 08:51:30.546974

"""
from alembic import op
from sqlalchemy import Column
from sqlalchemy import String


# revision identifiers, used by Alembic.
revision = 'ac151f9f2237'
down_revision = 'f04372fa8f80'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table("events") as batch_op:
        batch_op.add_column(Column('arg', String))
        batch_op.add_column(Column('description', String))


def downgrade():
    pass
