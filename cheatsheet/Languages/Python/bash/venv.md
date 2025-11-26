`venv` помогает избежать конфликтов между различными проектами, предоставляя каждому из них своё собственное пространство для зависимостей

### Создание виртуального окружения

```bash
python -m venv venv
```

### Активация окружения

- **Windows:** ```bash
venv\Scripts\activate
```
- **macOS/Linux:** ```
source venv/bin/activate
```

### Деактивация окружения

```bash
deactivate
```

### Установка пакетов в окружении из [[Languages/Python/bash/requirements.txt]]

```bash
pip install -r requirements.txt
```

### Удаление окружения

Просто удалите папку с виртуальным окружением `venv`

- **Windows:** ```bash
rmdir /s /q venv
```
- **macOS/Linux:** ```bash
rm -rf venv
```
