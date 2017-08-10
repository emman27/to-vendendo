"""empty message

Revision ID: e08c456848ab
Revises: a696f054c9b3
Create Date: 2017-08-10 00:19:09.190303

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
from tovendendo.items.models import Item


# revision identifiers, used by Alembic.
revision = 'e08c456848ab'
down_revision = 'a696f054c9b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_categories_name'), 'categories', ['name'], unique=True)
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('manufacturer', sa.String(length=100), nullable=True),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('age', sqlalchemy_utils.types.choice.ChoiceType(Item.TYPES), nullable=True),
    sa.Column('available_on', sa.DateTime(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_items_name'), 'items', ['name'], unique=True)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('email', sqlalchemy_utils.types.email.EmailType(), nullable=True),
    sa.Column('phone_number', sqlalchemy_utils.types.phone_number.PhoneNumberType(), nullable=True),
    sa.Column('_password', sqlalchemy_utils.types.password.PasswordType(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('items_categories',
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('item_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.ForeignKeyConstraint(['item_id'], ['items.id'], )
    )
    op.drop_table('category')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='category_pkey')
    )
    op.drop_table('items_categories')
    op.drop_table('users')
    op.drop_index(op.f('ix_items_name'), table_name='items')
    op.drop_table('items')
    op.drop_index(op.f('ix_categories_name'), table_name='categories')
    op.drop_table('categories')
    # ### end Alembic commands ###
