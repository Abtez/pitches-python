"""migrating new data

Revision ID: 041a17bd8e6a
Revises: 6fd725da3ab2
Create Date: 2020-09-20 09:03:51.274614

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '041a17bd8e6a'
down_revision = '6fd725da3ab2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'bio')
    # ### end Alembic commands ###
