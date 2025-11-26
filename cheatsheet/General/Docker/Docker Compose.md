# Docker Compose

Docker Compose - инструмент для управления многоконтейнерными приложениями с помощью файла `docker-compose.yml`
Позволяет легко запускать, останавливать и управлять сервисами

## Установка Docker Compose
Если у вас установлен Docker, то Docker Compose уже встроен
Проверить версию
```bash
docker-compose version  # В старых версиях
docker compose version  # В новых версиях
```
## Базовая структура
`docker-compose.yml`
```yaml@docker-compose.yml
version: "3.8"  # Версия Docker Compose

services:
  app:
    image: python:3.10
    container_name: my_python_app
    working_dir: /app
    volumes:
      - .:/app
    command: python app.py
```
Запуск
```bash
docker compose up
```
Остановка
```bash
docker compose down
```
## Запуск нескольких сервисов
Пример: `Flask` + `PostgreSQL`
```yaml
version: "3.8"

services:
  db:
    image: postgres:15
    container_name: my_postgres
    restart: always
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: mydb
    volumes:
      - pgdata:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  app:
    build: .
    container_name: my_flask_app
    depends_on:
      - db
    ports:
      - "5000:5000"
    environment:
      DATABASE_URL: postgresql://user:password@db/mydb
    volumes:
      - .:/app
    command: python app.py

volumes:
  pgdata:
```
Запуск всех сервисов
```bash
docker compose up -d
```
Остановка всех сервисов
```bash
docker compose down
```

## `build` и `image`
- `image: python:3.10` - использовать готовый образ
- `build: .` - собирать из `Dockerfile`

### Пример `Dockerfile`
```dockerfile
FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```
Запуск
```bash
docker compose up --build
```
## Переменные окружения
Создаём файл `.env`
```ini@.env
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=mydb
```
Изменяем `docker-compose.yml`
```yaml@docker-compose.yml
environment:
  POSTGRES_USER: ${POSTGRES_USER}
  POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
  POSTGRES_DB: ${POSTGRES_DB}
```
## Логи и отладка
```bash
docker compose logs -f       # Логи всех контейнеров
docker compose logs app      # Логи конкретного контейнера
docker compose ps            # Список запущенных контейнеров
docker compose exec app bash # Открыть shell в контейнере
docker compose restart app   # Перезапустить сервис
```
## Запуск в продакшене
`restart` и `.env`-файл
```yaml
version: "3.8"

services:
  app:
    image: my_flask_app:latest
    restart: always
    env_file:
      - .env
```
Запуск
```bash
docker compose up -d
```
Остановка
```bash
docker compose down --remove-orphans
```
## Docker Compose + Nginx
Обратный прокси
Файл `docker-compose.yml`
```yaml@docker-compose.yml
version: "3.8"

services:
  nginx:
    image: nginx:latest
    container_name: my_nginx
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - app

  app:
    build: .
    container_name: my_flask_app
    environment:
      - DATABASE_URL=postgresql://user:password@db/mydb
    depends_on:
      - db

  db:
    image: postgres:15
    container_name: my_postgres
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: mydb
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```
Файл `nginx.conf`
```nginx@nginx.conf
events {}

http {
    server {
        listen 80;
        location / {
            proxy_pass http://app:5000;
        }
    }
}
```
Запуск
```bash
docker compose up -d
```
# Заключение
Docker Compose позволяет легко управлять многоконтейнерными приложениями,
обеспечивать их автоматический перезапуск и упрощает настройку сетевого взаимодействия
