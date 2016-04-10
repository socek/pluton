"""Add events

Revision ID: fb398eeaeffe
Revises: d2087b5a6d77
Create Date: 2016-04-10 16:24:15.544957

"""
from alembic import op
from datetime import datetime
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

# revision identifiers, used by Alembic.
revision = 'fb398eeaeffe'
down_revision = 'd2087b5a6d77'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'events',
        Column(
            'id',
            Integer,
            primary_key=True
        ),
        Column(
            'name',
            String,
            nullable=False,
        ),

        Column(
            'data',
            String
        ),
        Column(
            'state',
            String,
            nullable=False,
            default=0,
        ),
        Column(
            'when_created',
            DateTime,
            default=datetime.utcnow,
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
