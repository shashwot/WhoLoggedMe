"""Create logs table

Revision ID: 629d193e32ef
Revises: 
Create Date: 2025-02-09 18:46:15.401449

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "629d193e32ef"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "logs",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("ip_address", sa.String(length=100), nullable=False),
        sa.Column("city", sa.String(length=200), nullable=True),
        sa.Column("country", sa.String(length=200), nullable=True),
        sa.Column("latitude", sa.Float(), nullable=True),
        sa.Column("longitude", sa.Float(), nullable=True),
        sa.Column("timezone", sa.String(length=200), nullable=True),
        sa.Column("isp", sa.String(length=200), nullable=True),
        sa.Column("user_agent", sa.String(length=800), nullable=True),
        sa.Column("device_type", sa.String(length=200), nullable=True),
        sa.Column("browser", sa.String(length=200), nullable=True),
        sa.Column("os", sa.String(length=200), nullable=True),
        sa.Column("asn", sa.String(length=200), nullable=True),
        sa.Column("is_proxy", sa.Boolean(), nullable=True),
        sa.Column("http_method", sa.String(length=200), nullable=True),
        sa.Column("request_path", sa.String(length=200), nullable=True),
        sa.Column("referrer", sa.String(length=800), nullable=True),
        sa.Column("timestamp", sa.String(length=200), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    pass
