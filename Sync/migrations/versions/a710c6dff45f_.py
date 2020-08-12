"""empty message

Revision ID: a710c6dff45f
Revises: d3a6d72596da
Create Date: 2020-07-16 12:15:22.863591

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a710c6dff45f'
down_revision = 'd3a6d72596da'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userid', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_userid'), 'user', ['userid'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_userid'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###