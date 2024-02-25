"""Create Patients Table

Revision ID: 54141d4c44d5
Revises: 
Create Date: 2024-02-24 20:26:46.509295

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54141d4c44d5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
         'patients',
         sa.Column('id', sa.Integer, primary_key=True),
         sa.Column('first_name', sa.String(50), nullable=False),
         sa.Column('last_name', sa.String(50), nullable=False),
         sa.Column('email', sa.String(100), nullable=False),
         sa.Column('phone_number', sa.String(20), nullable=False),
         sa.Column('date_of_birth', sa.Date, nullable=False)
    )


def downgrade():
    op.drop_table('patients')
