"""Add 'language' field to User model

Revision ID: 62c6f3969137
Revises: 284ef29a9439
Create Date: 2021-07-10 18:20:41.726698

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62c6f3969137'
down_revision = '284ef29a9439'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('language', sa.String(length=10), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'language')
    # ### end Alembic commands ###
