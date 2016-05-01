"""Rename clients to endpoints.

Revision ID: a1d83bc371bb
Revises: 45778f751d09
Create Date: 2016-05-01 13:35:38.733749

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = 'a1d83bc371bb'
down_revision = '45778f751d09'
branch_labels = None
depends_on = None


def upgrade():
    op.rename_table('clients', 'endpoints')


def downgrade():
    pass
