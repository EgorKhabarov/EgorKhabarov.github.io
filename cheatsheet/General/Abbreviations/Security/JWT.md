# JWT
JSON Web Token
Токены авторизации
### Как работает JWT?
JWT состоит из трёх частей
```
header.payload.signature
```
Пример JWT
```json
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9

eyJ1c2VyX2lkIjoxMjMsInJvbGUiOiJ1c2VyIn0

SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```
### Плюсы JWT
- **Статическая аутентификация** — не требует запросов к базе данных
- **Гибкость** — можно использовать в API
### Минусы JWT:
- Нельзя просто отозвать токен без механизма чёрного списка
- Токен может быть украден при `XSS`-атаке
### Защита JWT:
- Использовать **`HttpOnly` и `Secure Cookies`** вместо `localStorage`
- Хранить срок жизни токена небольшим (например, 15 минут)
- Использовать `refresh`-токены