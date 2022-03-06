"""post body3

Revision ID: cce8fd357ffa
Revises: 28d73975ac59
Create Date: 2022-01-31 15:57:31.770965

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cce8fd357ffa'
down_revision = '28d73975ac59'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('body3', sa.String(length=140), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'body3')
    # ### end Alembic commands ###