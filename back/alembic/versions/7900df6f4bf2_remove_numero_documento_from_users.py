from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "7900df6f4bf2"
down_revision = "914bfd733f83"
branch_labels = None
depends_on = None


def upgrade():

    op.drop_column(
        "users",
        "numero_documento"
    )


def downgrade():

    op.add_column(

        "users",

        sa.Column(

            "numero_documento",

            sa.String(length=100),

            nullable=False
        )
    )