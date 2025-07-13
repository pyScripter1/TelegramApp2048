from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger
from typing import Optional
from app.database import Base


class User(Base):
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    username: Mapped[Optional[str]]
    first_name: Mapped[Optional[str]]
    last_name: Mapped[Optional[str]]
    best_score: Mapped[int] = mapped_column(default=0)  # Начальное значение наилучшего счета