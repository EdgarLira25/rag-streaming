from datetime import datetime
from sqlalchemy import CheckConstraint, Column, String, DateTime
from .base import Base


class UserDao(Base):
    __tablename__ = "user"
    __table_args__ = (
        CheckConstraint(
            "user_type IN ('admin', 'premium', 'common')", name="user_type_check"
        ),
    )
    email = Column(String(255), primary_key=True)
    name = Column(String(255))
    user_type = Column(String(10), default="common", nullable=False)
    secret_hash = Column(String(255))
    created_at = Column(DateTime, default=datetime.now)
