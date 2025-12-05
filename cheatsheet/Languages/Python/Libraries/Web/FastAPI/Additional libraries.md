# Таблица дополнительных библиотек для FastAPI

| Библиотека                                                     | Описание                                               |
|----------------------------------------------------------------|--------------------------------------------------------|
| `SlowAPI`<br>`pip install slowapi`                             | Ограничение количества запросов (Rate Limiting)        |
| `FastAPI-Security`<br>`pip install fastapi-security`           | Инструменты для безопасности, включая `OAuth2` и `JWT` |
| `fastapi.middleware.cors`<br>**Встроено в FastAPI**            | Встроенная поддержка `CORS`                            |
| `fastapi_jwt_auth`<br>`pip install fastapi-jwt-auth`           | Аутентификация через `JWT`                             |
| `starlette.middleware.trustedhost`<br>**Встроено в Starlette** | Ограничение доверенных хостов                          |
| `Tortoise-ORM`<br>`pip install tortoise-orm`                   | `ORM` для работы с базами данных                       |
| `SQLAlchemy`<br>`pip install sqlalchemy`                       | `ORM` для работы с базами данных                       |
| `Alembic`<br>`pip install alembic`                             | Управление миграциями базы данных                      |
| `Databases`<br>`pip install databases`                         | Асинхронная работа с базами данных                     |
| `FastAPI-SocketIO`<br>`pip install fastapi-socketio`           | Работа с `WebSocket`                                   |
| `fastapi-mail`<br>`pip install fastapi-mail`                   | Отправка `email`                                       |
| `aiocache`<br>`pip install aiocache`                           | Асинхронное кеширование данных                         |
| `APScheduler`<br>`pip install apscheduler`                     | Планирование задач (`cron`, интервалы)                 |

# Примеры использования
### Ограничение запросов
#### SlowAPI
[https://pypi.org/project/slowapi/](https://pypi.org/project/slowapi/)
```python
from fastapi import FastAPI
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware

app = FastAPI()
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

@app.get("/")
@limiter.limit("5/minute")
async def index():
    return {"message": "Hello, FastAPI!"}
```
### JWT-аутентификация
#### fastapi_jwt_auth
[https://pypi.org/project/fastapi-jwt-auth/](https://pypi.org/project/fastapi-jwt-auth/)
```python
from fastapi import FastAPI, Depends
from fastapi_jwt_auth import AuthJWT

app = FastAPI()

class Settings:
    authjwt_secret_key: str = "secret"

@AuthJWT.load_config
def get_config():
    return Settings()

@app.post("/login")
def login(Authorize: AuthJWT = Depends()):
    access_token = Authorize.create_access_token(subject="user1")
    return {"access_token": access_token}

@app.get("/protected")
def protected(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    return {"message": "This is protected"}
```
### Работа с базой данных
#### Tortoise-ORM
[https://pypi.org/project/tortoise-orm/](https://pypi.org/project/tortoise-orm/)
```python
from fastapi import FastAPI
from tortoise.models import Model
from tortoise import fields, Tortoise

app = FastAPI()

class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=80)

@app.on_event("startup")
async def startup():
    await Tortoise.init(db_url="sqlite://database.db", modules={"models": ["__main__"]})
    await Tortoise.generate_schemas()

@app.get("/")
async def index():
    users = await User.all()
    return {"users": [user.name for user in users]}
```
### Работа с WebSocket
#### FastAPI-SocketIO
[https://pypi.org/project/fastapi-socketio/](https://pypi.org/project/fastapi-socketio/)
```python
from fastapi import FastAPI
from fastapi_socketio import SocketManager

app = FastAPI()
socket_manager = SocketManager(app)

@app.sio.on("message")
async def handle_message(sid, data):
    print("Received:", data)
    await app.sio.emit("message", "Echo: " + data)

@app.get("/")
async def index():
    return {"message": "WebSocket server running"}
```
