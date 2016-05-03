"""Morf ReactionLink to EventGroup.

Revision ID: 674d17001699
Revises: 7cd89b82f45a
Create Date: 2016-05-03 18:25:08.135594

"""
from alembic import op
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer

# revision identifiers, used by Alembic.
revision = '674d17001699'
down_revision = '7cd89b82f45a'
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    conn.execute("delete from reaction_links")
    with op.batch_alter_table("reaction_links") as batch_op:
        batch_op.drop_column('endpoint_id')
        batch_op.drop_column('event_name')
        batch_op.add_column(
            Column(
                'event_group_id',
                Integer,
                ForeignKey('event_groups.id'),
                nullable=False,
            )
        )


def downgrade():
    pass
