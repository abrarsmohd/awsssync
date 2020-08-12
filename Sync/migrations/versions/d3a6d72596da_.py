"""empty message

Revision ID: d3a6d72596da
Revises: 03e04d5d54ab
Create Date: 2020-07-15 23:42:44.494306

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3a6d72596da'
down_revision = '03e04d5d54ab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_list_listitem', table_name='list')
    op.create_index(op.f('ix_list_listitem'), 'list', ['listitem'], unique=False)
    op.drop_index('ix_list_username', table_name='list')
    op.create_index(op.f('ix_list_username'), 'list', ['username'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_list_username'), table_name='list')
    op.create_index('ix_list_username', 'list', ['username'], unique=1)
    op.drop_index(op.f('ix_list_listitem'), table_name='list')
    op.create_index('ix_list_listitem', 'list', ['listitem'], unique=1)
    # ### end Alembic commands ###
