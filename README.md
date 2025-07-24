# TelegramApp2048

Захватывающая игра 2048 в TelegramMiniApps! Играй, побей рекорд и стань первым в таблице рекордов!

**Основные функции**
  * **Играйте в 2048:** Играйте в классическую игру прямо у себя в Telegram.
  * **Просмотр рекорда:** Возможность сохранить свой личный рекорд и посмотреть рекорд других пользователей.
  * **Хранилище данных:** Данные игры сохраняются в локальном хранилице MiniApp, что обеспечивает быстрый доступ и удобство продолжения игры.

**Стек технологий**
  * **Fastapi** - для реализации API методов и обработки вебхуков.
  * **Aiogram** - для создания и взаимодействия с Telegram ботом и обработки сообщений.
  * **SqlAlchemy + Alembic** - для работы с базой данных и управления миграциями.
  * **SQLite** - база данных для хранения рекордов пользователей.

**Переменные окружения**
Проект использует файл .env для хранения конфиденциальных данных. Пример содержимого файла:
```
BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
BASE_SITE=https://your-base-url.io
ADMIN_IDS=[ADMINid1, ADMINid2]
```
* BOT_TOKEN — токен Telegram-бота.
* BASE_SITE — базовый URL для MiniApp и вебхуков.
* ADMIN_IDS — Список из TelegramIDs администраторов.

**Установка проекта**
**1. Склонируй репозиторий**
```
git clone https://github.com/pyScripter1/TelegramApp2048.git
cd TelegramApp2048
```
**2. Установите зависимости**
`pip install -r requirements.txt`
**3. Создайте файл .env с вашими настройками**
**4. Запустите приложение**
`uvicorn app.main:app --reload`

**Зависимости**
В проекте следующие зависимости:
```
aiogram==3.13.1
fastapi==0.115.0
pydantic==2.9.2
uvicorn==0.31.0
jinja2==3.1.4
pydantic_settings==2.5.2
aiosqlite==0.20.0
alembic==1.13.3
loguru==0.7.2
SQLAlchemy==2.0.35
```

**Пример работы**

<img width="450" height="350" alt="image" src="https://github.com/user-attachments/assets/78af24c3-fd92-4085-b332-b0241c818604" />
<img width="469" height="818" alt="image" src="https://github.com/user-attachments/assets/354ad0cd-bf9e-4e2f-b892-8e820092b7b7" />

**Протестировать игру можно здесь:**





