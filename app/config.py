import os
from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    BOT_TOKEN : str
    ADMIN_ID : List[int]
    DB_URL: str = "sqlite+aiosqlite:///data/db.sqlite3"
    BASE_SITE : str

    model_config = SettingsConfigDict(
        env_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env")
    )

    def webhook_url(self) -> str:
        """Возвращает url вебхука с кодированием специальных символов."""
        return f"{self.BASE_SITE}/webhook"

# Получаем параметры для загрузки переменных среды
settings = Settings()
database_url = settings.DB_URL
