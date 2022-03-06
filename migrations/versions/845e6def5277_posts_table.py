"""posts table

Revision ID: 845e6def5277
Revises: 8b60a5dee790
Create Date: 2022-02-02 21:17:27.091353

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '845e6def5277'
down_revision = '8b60a5dee790'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('project', sa.String(length=100), nullable=True))
    op.add_column('post', sa.Column('progress', sa.String(length=100), nullable=True))
    op.add_column('post', sa.Column('problem', sa.String(length=100), nullable=True))
    op.add_column('post', sa.Column('plan', sa.String(length=100), nullable=True))
    op.drop_column('post', 'body2')
    op.drop_column('post', 'body3')
    op.drop_column('post', 'body4')
    op.drop_column('post', 'body1')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('body1', sa.VARCHAR(length=140), nullable=True))
    op.add_column('post', sa.Column('body4', sa.VARCHAR(length=140), nullable=True))
    op.add_column('post', sa.Column('body3', sa.VARCHAR(length=140), nullable=True))
    op.add_column('post', sa.Column('body2', sa.VARCHAR(length=140), nullable=True))
    op.drop_column('post', 'plan')
    op.drop_column('post', 'problem')
    op.drop_column('post', 'progress')
    op.drop_column('post', 'project')
    # ### end Alembic commands ###
