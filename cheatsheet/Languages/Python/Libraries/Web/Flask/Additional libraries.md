# Таблица дополнительных библиотек для Flask

| Библиотека           | Описание                                                     | Установка                        |
|----------------------|--------------------------------------------------------------|----------------------------------|
| `Flask-Limiter`      | Ограничение количества запросов (Rate Limiting)              | `pip install flask-limiter`      |
| `Flask-Security-Too` | Аутентификация, управление пользователями и защита от атак   | `pip install flask-security-too` |
| `Flask-CORS`         | Обработка `CORS` (разрешение междоменных запросов)           | `pip install flask-cors`         |
| `Flask-JWT-Extended` | Аутентификация через `JWT` (JSON Web Tokens)                 | `pip install flask-jwt-extended` |
| `Flask-Talisman`     | Улучшение безопасности через заголовки (`CSP`, `HSTS` и др.) | `pip install flask-talisman`     |
| `Flask-SQLAlchemy`   | Работа с базой данных через `ORM`                            | `pip install flask-sqlalchemy`   |
| `Flask-Migrate`      | Управление миграциями базы данных                            | `pip install flask-migrate`      |
| `Flask-SocketIO`     | Работа с `WebSocket`                                         | `pip install flask-socketio`     |
| `Flask-RESTful`      | Упрощение создания `REST API`                                | `pip install flask-restful`      |
| `Flask-Mail`         | Отправка `email`                                             | `pip install flask-mail`         |
| `Flask-Caching`      | Кеширование данных                                           | `pip install flask-caching`      |
| `Flask-APScheduler`  | Планирование задач (`cron`, интервалы)                       | `pip install flask-apscheduler`  |

# Примеры использования
### Ограничение запросов
#### Flask-Limiter
[https://pypi.org/project/Flask-Limiter/](https://pypi.org/project/Flask-Limiter/)
```python
from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(get_remote_address, app=app, default_limits=["5 per minute"], storage_uri="memory://")

@app.route("/")
@limiter.limit("2 per second")
def index():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run()
```
### JWT-аутентификация
#### Flask-JWT-Extended
[https://pypi.org/project/Flask-JWT-Extended/](https://pypi.org/project/Flask-JWT-Extended/)
```python
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "secret"
jwt = JWTManager(app)

@app.route("/login")
def login():
    access_token = create_access_token(identity="user1")
    return jsonify(access_token=access_token)

@app.route("/protected")
@jwt_required()
def protected():
    return jsonify(message="This is protected")

if __name__ == "__main__":
    app.run()
```
### Работа с базой данных
#### Flask-SQLAlchemy
[https://pypi.org/project/Flask-SQLAlchemy/](https://pypi.org/project/Flask-SQLAlchemy/)
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

@app.route("/")
def index():
    return {"users": [user.name for user in User.query.all()]}

if __name__ == "__main__":
    db.create_all()
    app.run()
```
### Работа с WebSocket
#### Flask-SocketIO
[https://pypi.org/project/Flask-SocketIO/](https://pypi.org/project/Flask-SocketIO/)
```python
from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on("message")
def handle_message(data):
    print("Received:", data)
    socketio.send("Echo: " + data)

if __name__ == "__main__":
    socketio.run(app)
```
