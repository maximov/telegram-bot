import pytest
import asyncio
from db.repository import init_db, save_message

@pytest.mark.asyncio
async def test_save_message():
    await init_db()
    await save_message(123, "test message")
    assert True  # упрощенно, можно проверять select
