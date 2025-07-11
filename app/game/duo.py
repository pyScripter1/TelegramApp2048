from pydantic import BaseModel
from sqlalchemy import select, desc, func
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import Base
from app.game.models import User


class UserDAO(Base):
    model = User