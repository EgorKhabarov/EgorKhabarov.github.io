# SSRF
Server-Side Request Forgery
Подделка серверных запросов
### Суть атаки
Злоумышленник заставляет сервер делать запросы к внутренним сервисам
### Пример уязвимости
```python
import requests
url = request.args.get("url")
response = requests.get(url)
```
Запрос `?url=http://localhost/admin` может позволить злоумышленнику получить доступ к внутреннему API

### Защита от SSRF
- Ограничение доступа к локальным адресам (`localhost`, `127.0.0.1`)
- Фильтрация входных URL
- Использование `allowlist`
