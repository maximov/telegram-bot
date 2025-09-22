import os

import asyncpg

# Получаем URL подключения
DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://postgres:postgres@db:5432/postgres"
)

_pool = None


async def init_db():
    global _pool
    _pool = await asyncpg.create_pool(DATABASE_URL)
    async with _pool.acquire() as conn:
        # создаем таблицу сообщений
        await conn.execute(
            """
        CREATE TABLE IF NOT EXISTS messages (
            id SERIAL PRIMARY KEY,
            user_id BIGINT NOT NULL,
            text TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT now()
        );
        """
        )


async def save_message(user_id: int, text: str):
    async with _pool.acquire() as conn:
        query = "INSERT INTO messages(user_id, text) VALUES ($1, $2)"
        await conn.execute(
            query, user_id, text
        )
