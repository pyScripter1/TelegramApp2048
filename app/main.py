from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.game.router import router as game_router

app = FastAPI()

# Монтируем статические файлы
app.mount('/static', StaticFiles(directory='app/static'), 'static')

# Подключаем роутер игры
app.include_router(game_router)