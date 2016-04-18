"""Add reaction link

Revision ID: 5fc434bc8b4e
Revises: 4dfd0e1d8ec4
Create Date: 2016-04-18 16:28:09.139623

"""
from alembic import op
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

# revision identifiers, used by Alembic.
revision = '5fc434bc8b4e'
down_revision = '4dfd0e1d8ec4'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'reaction_links',
        Column(
            'id',
            Integer,
            primary_key=True
        ),
        Column(
            'priority',
            Integer,
            nullable=False,
            default=0
        ),
        Column(
            'reaction_name',
            String,
            nullable=False
        ),
        Column(
            'event_name',
            String,
            nullable=False
        ),
        Column(
            'client_id',
            Integer,
            ForeignKey('clients.id'),
            nullable=False,
        ),
    )


def downgrade():
    pass
