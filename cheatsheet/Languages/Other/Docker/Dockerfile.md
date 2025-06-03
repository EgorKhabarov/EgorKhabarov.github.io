Dockerfile
FROM:    Определяет базовый образ, на основе которого будет создан ваш образ контейнера.
         Здесь мы используем образ `Python 3.9` на основе `slim-версии Debian`.

WORKDIR: Устанавливает рабочую директорию внутри контейнера, где будут выполняться команды.

COPY:    Копирует файлы из текущей директории на вашем компьютере внутрь контейнера.

RUN:     Выполняет команды внутри контейнера для установки зависимостей, указанных в файле `requirements.txt`.

CMD:     Определяет команду, которая будет запущена при запуске контейнера.
         Здесь мы указываем запуск основного скрипта `main.py`.

```Dockerfile@Dockerfile
FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "main.py"]
```


```Dockerfile
ENV BOT_TOKEN=""
```

![docker.png](Languages/Other/Dockerfile/docker.png)
