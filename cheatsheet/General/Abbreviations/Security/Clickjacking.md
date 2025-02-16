# Clickjacking
Перехват кликов
### Суть атаки
Злоумышленник вставляет страницу жертвы в `<iframe>` и накладывает прозрачные элементы, перенаправляя клики
### Защита от Clickjacking:
- **HTTP-заголовок `X-Frame-Options: DENY`**
- **Content Security Policy (CSP)**
