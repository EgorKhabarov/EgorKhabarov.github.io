# Dockerfile
### FROM
Определяет базовый образ, на основе которого будет создан ваш образ контейнера
Здесь мы используем образ `Python 3.9` на основе `slim-версии Debian`

### WORKDIR
Устанавливает рабочую директорию внутри контейнера, где будут выполняться команды

### COPY
Копирует файлы из текущей директории на вашем компьютере внутрь контейнера

### RUN
Выполняет команды внутри контейнера для установки зависимостей, указанных в файле `requirements.txt`

### CMD
Определяет команду, которая будет запущена при запуске контейнера
Здесь мы указываем запуск основного скрипта `main.py`

```Dockerfile@Dockerfile
FROM python:3.13-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
RUN useradd --create-home --shell /bin/bash appuser
COPY requirements.txt .
RUN pip install --no-cache-dir -U pip && \
    pip install --no-cache-dir -r requirements.txt
COPY . .
RUN chown -R appuser:appuser /app
USER appuser
EXPOSE 8000
CMD ["python", "app.py"]
```


```Dockerfile
ENV BOT_TOKEN=""
```


| Command   | Purpose                                            |
|-----------|----------------------------------------------------|
| `FROM`    | Specifies the base image                           |
| `WORKDIR` | Sets the working directory                         |
| `COPY`    | Copies files/directories into the container        |
| `RUN`     | Executes commands during image building            |
| `EXPOSE`  | Exposes ports                                      |
| `CMD`     | Specifies the default command to run               |
| `ENV`     | Sets environment variables                         |
| `ARG`     | Defines build-time variables                       |
| `LABEL`   | Adds metadata to the image                         |
| `VOLUME`  | Creates a mount point as a volume in the container |
