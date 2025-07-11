from datetime import datetime
from sqlalchemy import func, TIMESTAMP, Integer
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine, AsyncSession
from app.config import database_url
from functools import wraps

# создание асинхронного движка для подключения к базе данных
engine = create_async_engine(url=database_url)
# фабрика асинхронных сессий, нужна для создания сессий для запросов к бд
async_session_maker = async_sessionmaker(engine, class_=AsyncSession)

# фабрика декораторов
def connection(isolation_level=None):
    def decorator(method):
        @wraps(method)
        async def wrapper(*args, **kwargs):
            async with async_session_maker() as session:
                try:
                    # Устанавливаем уровень изоляции, если передан
                    if isolation_level:
                        await session.execute(text(f"SET TRANSACTION ISOLATION LEVEL {isolation_level}"))
                    # Выполняем декорированный метод
                    return await method(*args, session=session, **kwargs)
                except Exception as e:
                    await session.rollback()  # Откатываем сессию при ошибке
                    raise e  # Поднимаем исключение дальше
                finally:
                    await session.close()  # Закрываем сессию

        return wrapper
    return decorator

# абстрактный класс для моделей ORM. Будет родительским для всех моделей таблиц
class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True # абстрактный класс чтобы измежать создание отдельной таблицы

    id: Mapped[int] = mapped_column(Integer, primary_key = True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, server_default=func.now(), onupdate=func.now()
    )

    @classmethod
    @property
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + "s"