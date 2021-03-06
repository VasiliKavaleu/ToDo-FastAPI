"""Added renamed library models

Revision ID: 04204981db9e
Revises: 577336ea467c
Create Date: 2021-06-15 15:53:31.542613

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04204981db9e'
down_revision = '577336ea467c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('covers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(), nullable=False),
    sa.Column('artist', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('readers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cover_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('author', sa.String(length=30), nullable=False),
    sa.Column('want_to_read', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['cover_id'], ['covers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reader_book',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['readers.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'book_id')
    )
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=3000), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['readers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    op.drop_table('reader_book')
    op.drop_table('books')
    op.drop_table('readers')
    op.drop_table('covers')
    # ### end Alembic commands ###
