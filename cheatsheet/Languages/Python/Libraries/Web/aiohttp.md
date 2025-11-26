# AIOHTTP
aiohttp асинхронный фреймворк для работы с HTTP в Python
Он позволяет писать высокопроизводительные веб-приложения и API, а также выполнять асинхронные HTTP-запросы
## Установка
```bash
pip install aiohttp
```
## Клиент AIOHTTP (отправка HTTP-запросов)
### Простой GET-запрос
```python
import aiohttp
import asyncio

async def fetch():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://jsonplaceholder.typicode.com/todos/1") as response:
            data = await response.json()
            print(data)

asyncio.run(fetch())
```
### POST-запрос с JSON
```python
async def post_data():
    async with aiohttp.ClientSession() as session:
        async with session.post("https://httpbin.org/post", json={"key": "value"}) as response:
            print(await response.json())

asyncio.run(post_data())
```
### Передача заголовков и параметров запроса
```python
async def fetch_with_headers():
    headers = {"Authorization": "Bearer YOUR_TOKEN"}
    params = {"q": "python"}

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get("https://api.example.com/search", params=params) as response:
            print(await response.text())

asyncio.run(fetch_with_headers())
```
### Загрузка файлов
```python
async def download_file():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://example.com/file.zip") as response:
            with open("file.zip", "wb") as f:
                while chunk := await response.content.read(1024):
                    f.write(chunk)

asyncio.run(download_file())
```
### Отправка файлов
```python
async def upload_file():
    async with aiohttp.ClientSession() as session:
        with open("file.txt", "rb") as f:
            data = aiohttp.FormData()
            data.add_field("file", f, filename="file.txt")

            async with session.post("https://httpbin.org/post", data=data) as response:
                print(await response.json())

asyncio.run(upload_file())
```
## Сервер на AIOHTTP
### Минимальный сервер
```python
from aiohttp import web

async def hello(request):
    return web.Response(text="Hello, AIOHTTP!")

app = web.Application()
app.add_routes([web.get("/", hello)])

web.run_app(app, port=8080)
```
### Обработка JSON-запросов
```python
async def handle_post(request):
    data = await request.json()
    return web.json_response({"received": data})

app = web.Application()
app.add_routes([web.post("/data", handle_post)])

web.run_app(app, port=8080)
```
### Маршрутизация с переменными
```python
async def greet(request):
    name = request.match_info["name"]
    return web.Response(text=f"Hello, {name}!")

app = web.Application()
app.add_routes([web.get("/hello/{name}", greet)])

web.run_app(app, port=8080)
```
### Middleware (Промежуточные обработчики)
```python
@web.middleware
async def auth_middleware(request, handler):
    if request.headers.get("Authorization") != "Bearer secret":
        return web.Response(text="Unauthorized", status=401)
    return await handler(request)

app = web.Application(middlewares=[auth_middleware])
app.add_routes([web.get("/", lambda _: web.Response(text="Welcome!"))])

web.run_app(app, port=8080)
```
### Обработка ошибок
```python
async def handle_404(request):
    return web.Response(text="Not Found", status=404)

app = web.Application()
app.add_routes([web.get("/", lambda _: web.Response(text="OK"))])
app.router.add_static("/static", "path/to/static")  # Статические файлы
app.router.add_routes([web.view("/404", handle_404)])

web.run_app(app, port=8080)
```
## WebSockets в AIOHTTP
### WebSocket-сервер
```python
async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            await ws.send_str(f"Received: {msg.data}")
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print(f"WS error: {ws.exception()}")

    return ws

app = web.Application()
app.add_routes([web.get("/ws", websocket_handler)])

web.run_app(app, port=8080)
```
### WebSocket-клиент
```python
async def ws_client():
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect("http://localhost:8080/ws") as ws:
            await ws.send_str("Hello, WebSocket!")
            msg = await ws.receive()
            print(f"Received: {msg.data}")

asyncio.run(ws_client())
```
## Работа с базами данных (пример с SQLite)
```python
import aiosqlite

async def fetch_data():
    async with aiosqlite.connect("database.db") as db:
        async with db.execute("SELECT * FROM users") as cursor:
            async for row in cursor:
                print(row)

asyncio.run(fetch_data())
```
## Запуск нескольких задач (asyncio.gather)
```python
async def task1():
    await asyncio.sleep(1)
    print("Task 1 done")

async def task2():
    await asyncio.sleep(2)
    print("Task 2 done")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())
```
## Завершение сессии корректно
При использовании `ClientSession()` лучше создавать **одну сессию** и использовать её повторно
```python
session = aiohttp.ClientSession()

async def fetch():
    async with session.get("https://example.com") as response:
        return await response.text()

# Закрываем сессию при выходе
async def close_session():
    await session.close()

asyncio.run(close_session())
```
# Заключение
AIOHTTP мощный инструмент для асинхронного взаимодействия с HTTP
Он полезен для создания API, работы с WebSockets и выполнения асинхронных запросов
