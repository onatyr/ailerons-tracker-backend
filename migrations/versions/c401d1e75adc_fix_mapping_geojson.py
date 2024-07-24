"""fix mapping geojson

Revision ID: c401d1e75adc
Revises: 5d3709f7bec9
Create Date: 2024-07-22 15:33:44.650719

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'c401d1e75adc'
down_revision = '5d3709f7bec9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    op.drop_table('point_geojson')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('individual', schema=None) as batch_op:
        batch_op.alter_column('id',
                              existing_type=sa.BIGINT(),
                              server_default=sa.Identity(
                                  always=True, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1),
                              existing_nullable=False,
                              autoincrement=True)

    op.create_table('spatial_ref_sys',
                    sa.Column('srid', sa.INTEGER(),
                              autoincrement=False, nullable=False),
                    sa.Column('auth_name', sa.VARCHAR(length=256),
                              autoincrement=False, nullable=True),
                    sa.Column('auth_srid', sa.INTEGER(),
                              autoincrement=False, nullable=True),
                    sa.Column('srtext', sa.VARCHAR(length=2048),
                              autoincrement=False, nullable=True),
                    sa.Column('proj4text', sa.VARCHAR(length=2048),
                              autoincrement=False, nullable=True),
                    sa.CheckConstraint('srid > 0 AND srid <= 998999',
                                       name='spatial_ref_sys_srid_check'),
                    sa.PrimaryKeyConstraint(
                        'srid', name='spatial_ref_sys_pkey')
                    )
    op.create_table('point_geojson',
                    sa.Column('id', sa.BIGINT(), sa.Identity(always=True, start=1, increment=1, minvalue=1,
                              maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
                    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text(
                        'now()'), autoincrement=False, nullable=False),
                    sa.Column('individual_id', sa.BIGINT(),
                              autoincrement=False, nullable=False),
                    sa.Column('record_id', sa.BIGINT(),
                              autoincrement=False, nullable=False),
                    sa.Column('geojson', postgresql.JSON(astext_type=sa.Text()),
                              autoincrement=False, nullable=False),
                    sa.ForeignKeyConstraint(
                        ['individual_id'], ['individual.id'], name='point_geojson_individual_id_fkey'),
                    sa.ForeignKeyConstraint(
                        ['record_id'], ['record.id'], name='point_geojson_record_id_fkey'),
                    sa.PrimaryKeyConstraint('id', name='point_geojson_pkey'),
                    sa.UniqueConstraint('id', name='point_geojson_id_key')
                    )
    op.create_table('article',
                    sa.Column('id', sa.BIGINT(), sa.Identity(always=True, start=1, increment=1, minvalue=1,
                              maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
                    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text(
                        'now()'), autoincrement=False, nullable=False),
                    sa.Column('archived', sa.BOOLEAN(), server_default=sa.text(
                        'false'), autoincrement=False, nullable=False),
                    sa.Column('published', sa.BOOLEAN(), server_default=sa.text(
                        'false'), autoincrement=False, nullable=False),
                    sa.Column('content', sa.TEXT(),
                              autoincrement=False, nullable=False),
                    sa.Column('title', sa.TEXT(),
                              autoincrement=False, nullable=False),
                    sa.Column('publication_date', postgresql.TIMESTAMP(),
                              autoincrement=False, nullable=False),
                    sa.Column('image_url', sa.TEXT(),
                              autoincrement=False, nullable=False),
                    sa.CheckConstraint('length(content) > 1',
                                       name='article_content_check'),
                    sa.PrimaryKeyConstraint('id', name='article_pkey'),
                    sa.UniqueConstraint('id', name='article_id_key')
                    )
    op.create_table('geo',
                    sa.Column('Name', sa.TEXT(),
                              autoincrement=False, nullable=True),
                    sa.Column('Description', sa.TEXT(),
                              autoincrement=False, nullable=True),
                    sa.Column('geometry', sa.NullType(),
                              autoincrement=False, nullable=True),
                    sa.Column('individual_id', sa.TEXT(),
                              autoincrement=False, nullable=True),
                    sa.Column('csv_uuid', sa.TEXT(),
                              autoincrement=False, nullable=True),
                    sa.Column('Date', sa.TEXT(),
                              autoincrement=False, nullable=True),
                    sa.Column('Observed Depth', sa.DOUBLE_PRECISION(
                        precision=53), autoincrement=False, nullable=True)
                    )
    with op.batch_alter_table('geo', schema=None) as batch_op:
        batch_op.create_index('idx_geo_geometry', [
                              'geometry'], unique=False, postgresql_using='gist')

    # ### end Alembic commands ###
