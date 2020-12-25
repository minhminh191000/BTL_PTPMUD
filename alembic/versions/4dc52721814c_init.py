"""init

Revision ID: 4dc52721814c
Revises: 8b9dfaa686f6
Create Date: 2020-12-02 15:50:26.115478

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4dc52721814c'
down_revision = '8b9dfaa686f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subjects', sa.Column('Student_id', postgresql.UUID(as_uuid=True), nullable=True))
    op.create_foreign_key(None, 'subjects', 'student', ['Student_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'subjects', type_='foreignkey')
    op.drop_column('subjects', 'Student_id')
    # ### end Alembic commands ###