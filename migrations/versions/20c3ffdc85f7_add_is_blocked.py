"""add is_blocked

Revision ID: 20c3ffdc85f7
Revises: 674d17001699
Create Date: 2016-09-20 20:44:03.277664

"""
from alembic import op
from sqlalchemy import Boolean
from sqlalchemy import Column


# revision identifiers, used by Alembic.
revision = '20c3ffdc85f7'
down_revision = '674d17001699'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table("event_groups") as batch_op:
        batch_op.add_column(Column('is_blocked', Boolean, default=False))


def downgrade():
    pass
