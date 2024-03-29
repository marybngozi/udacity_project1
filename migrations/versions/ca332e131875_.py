"""empty message

Revision ID: ca332e131875
Revises: 0d6a02fbb3fd
Create Date: 2022-04-21 21:56:37.671795

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca332e131875'
down_revision = '0d6a02fbb3fd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artist', sa.Column('created_on', sa.DateTime(), nullable=True))
    op.add_column('venue', sa.Column('created_on', sa.DateTime(), nullable=True))
    op.execute("UPDATE artist SET created_on = '2022-04-21 21:17:31.707970' WHERE created_on IS NULL;")
    op.execute("UPDATE venue SET created_on = '2022-04-21 21:17:31.707970' WHERE created_on IS NULL;")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venue', 'created_on')
    op.drop_column('artist', 'created_on')
    # ### end Alembic commands ###
