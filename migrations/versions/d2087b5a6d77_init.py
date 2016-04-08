"""init

Revision ID: d2087b5a6d77
Revises:
Create Date: 2016-04-08 21:55:25.027189

"""
from alembic import op
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

# revision identifiers, used by Alembic.
revision = 'd2087b5a6d77'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'clients',
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
            'api_key',
            String,
            nullable=False,
        ),
        Column(
            'api_secret',
            String,
            nullable=False,
        )
    )


def downgrade():
    pass
