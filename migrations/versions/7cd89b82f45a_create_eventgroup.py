"""Create EventGroup

Revision ID: 7cd89b82f45a
Revises: c8c1daae3ec3
Create Date: 2016-05-01 21:28:30.208086

"""
from alembic import op
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import JSON

# revision identifiers, used by Alembic.
revision = '7cd89b82f45a'
down_revision = 'c8c1daae3ec3'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'event_groups',
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
            'arg',
            String,
        ),
        Column(
            'state',
            String,
            nullable=False,
            default='normal',
        ),

        Column(
            'is_hidden',
            Boolean,
            default=False
        ),

        Column(
            'reaction_data',
            JSON,
        ),

        Column(
            'description',
            String,
        ),
        Column(
            'endpoint_id',
            Integer,
            ForeignKey('endpoints.id'),
            nullable=False,
        )
    )

    conn = op.get_bind()
    conn.execute("delete from events")

    with op.batch_alter_table("events") as batch_op:
        batch_op.drop_column('state')
        batch_op.drop_column('endpoint_id')
        batch_op.drop_column('reaction_data')
        batch_op.drop_column('arg')
        batch_op.drop_column('name')
        batch_op.drop_column('description')
        batch_op.drop_column('is_hidden')

        batch_op.add_column(
            Column(
                'group_id',
                Integer,
                ForeignKey('event_groups.id'),
                nullable=False,
            )
        )


def downgrade():
    pass
