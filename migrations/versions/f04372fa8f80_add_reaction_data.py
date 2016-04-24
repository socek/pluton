"""Add reaction_data

Revision ID: f04372fa8f80
Revises: 5fc434bc8b4e
Create Date: 2016-04-24 21:32:30.039362

"""
from alembic import op
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import JSON


# revision identifiers, used by Alembic.
revision = 'f04372fa8f80'
down_revision = '5fc434bc8b4e'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table("events") as batch_op:
        batch_op.add_column(Column('reaction_data', JSON))


def downgrade():
    pass
