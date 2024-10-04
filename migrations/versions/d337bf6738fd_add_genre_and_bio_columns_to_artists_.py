"""Add genre and bio columns to artists table

Revision ID: d337bf6738fd
Revises: 509c51be87f8
Create Date: 2024-10-04 13:55:56.589132

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd337bf6738fd'
down_revision = '509c51be87f8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artists', sa.Column('genre', sa.String(), nullable=True))
    op.add_column('artists', sa.Column('bio', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('artists', 'bio')
    op.drop_column('artists', 'genre')
    # ### end Alembic commands ###
