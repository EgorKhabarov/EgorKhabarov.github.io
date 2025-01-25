```bash
# SQLAlchemy
pip install sqlalchemy

# MySQL
pip install pymysql
# PostgreSQL
pip install psycopg2
```

```python
"sqlite:///example.db"
"mysql+pymysql://<user>:<password>@<host>/<database>"
"postgresql+psycopg2://<user>:<password>@<host>/<database>"
```

```bash
# SQLAlchemy
pip install sqlalchemy[asyncio]

# SQLite
pip install aiosqlite
# MySQL
pip install aiomysql
# PostgreSQL
pip install asyncpg
```

```python
"sqlite+aiosqlite:///example.db"
"mysql+aiomysql://<user>:<password>@<host>/<database>"
"postgresql+asyncpg://<user>:<password>@<host>/<database>"
```

```python
from contextlib import contextmanager

from sqlalchemy import create_engine, text, Engine
from sqlalchemy.orm import sessionmaker, Session

from config import SQLITE_DATABASE_URL


sqlite_engine: Engine = create_engine(SQLITE_DATABASE_URL, echo=False)
new_sqlite_session_func = sessionmaker(bind=sqlite_engine, expire_on_commit=False)


@contextmanager
def get_sqlite_session() -> Session:
    with new_sqlite_session_func() as sqlite_session:
        yield sqlite_session


def get_item(item_id: int) -> list:
    with get_sqlite_session() as session:
        result = session.execute(
            text("SELECT * FROM items WHERE item_id = :item_id"),
            {"item_id": item_id},
        )
        return result.fetchone()

```

```python
from contextlib import asynccontextmanager

from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncEngine

from config import SQLITE_DATABASE_URL


sqlite_engine: AsyncEngine = create_async_engine(SQLITE_DATABASE_URL, echo=False)
new_sqlite_async_session_func = async_sessionmaker(sqlite_engine, expire_on_commit=False)


@asynccontextmanager
async def get_sqlite_session():
    async with new_sqlite_async_session_func() as sqlite_session:
        yield sqlite_session


async def get_item(item_id: int) -> list:
    async with get_sqlite_session() as session:
        result = await session.execute(
            text("SELECT * FROM items WHERE item_id = :item_id"),
            {"item_id": item_id},
        )
        return result.fetchone()

```
