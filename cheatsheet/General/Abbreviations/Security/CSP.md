# Content Security Policy (CSP)

`Content Security Policy` (`CSP`) — это механизм защиты от атак, таких как XSS (межсайтовый скриптинг),
путем явного указания, какие ресурсы можно загружать и откуда

# Как работает CSP?
CSP добавляется через заголовок `Content-Security-Policy` или `<meta>`-тег в HTML
Он указывает, какие источники разрешены для скриптов, стилей, изображений и других ресурсов

### Пример заголовка:
```http
Content-Security-Policy: default-src 'self'; script-src 'self' https://apis.google.com
```

Аналог через `<meta>`:
```html
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' https://apis.google.com">
```

# Директивы CSP
### Базовые директивы
| Директива     | Описание                                                                    |
|---------------|-----------------------------------------------------------------------------|
| `default-src` | Базовый источник для всех типов контента (если другие директивы не указаны) |
| `script-src`  | Разрешенные источники `JavaScript`                                          |
| `style-src`   | Разрешенные источники `CSS`                                                 |
| `img-src`     | Разрешенные источники изображений                                           |
| `media-src`   | Разрешенные источники аудио и видео                                         |
| `connect-src` | Разрешенные источники для `fetch()`, WebSockets и XHR                       |
| `font-src`    | Разрешенные источники шрифтов                                               |
| `frame-src`   | Разрешенные источники для `<iframe>`                                        |
| `object-src`  | Разрешенные источники для `<object>`, `<embed>`, `<applet>`                 |
| `worker-src`  | Разрешенные источники для Web Workers                                       |

### Политики источников
| Политика          | Описание                                           |
|-------------------|----------------------------------------------------|
| `'self'`          | Разрешает ресурсы с того же домена                 |
| `'none'`          | Запрещает загрузку любых ресурсов                  |
| `'unsafe-inline'` | Разрешает встроенные стили и скрипты (НЕБЕЗОПАСНО) |
| `'unsafe-eval'`   | Разрешает `eval()` в `JavaScript` (НЕБЕЗОПАСНО)    |
| `https:`          | Разрешает загрузку только через HTTPS              |
| `data:`           | Разрешает `data:`-URL (НЕБЕЗОПАСНО)                |
| `blob:`           | Разрешает `blob:`-URL                              |

# Примеры CSP
### Запрещаем всё, кроме безопасных источников
```http
Content-Security-Policy: default-src 'self'; script-src 'self' https://trusted.cdn.com; style-src 'self'
```
- Разрешены скрипты только с `self` и `trusted.cdn.com`
- Стили разрешены только с `self`
- Все остальные ресурсы заблокированы

### Разрешаем загрузку изображений с любых источников
```http
Content-Security-Policy: img-src *;
```

### Разрешаем только HTTPS
```http
Content-Security-Policy: default-src https:;
```

### Запрещаем inline-скрипты и `eval()`
```http
Content-Security-Policy: script-src 'self';
```

# Режим "только отчёт" (report-only)
Можно протестировать `CSP`, не блокируя ресурсы:
```http
Content-Security-Policy-Report-Only: default-src 'self'; script-src 'self'; report-uri /csp-report
```
Браузер отправит отчёты о нарушениях на `/csp-report`, но ничего не заблокирует

## Как избежать ошибок CSP?
- **Не используйте `unsafe-inline`**: вместо этого используйте `nonce` или `hash`
- **Используйте `nonce` для разрешения конкретных inline-скриптов**
```http
Content-Security-Policy: script-src 'self' 'nonce-abc123';
```
```html
<script nonce="abc123">console.log('Безопасный inline-скрипт');</script>
```
- **Используйте `strict-dynamic` для безопасных загрузок скриптов**:
```http
Content-Security-Policy: script-src 'self' 'strict-dynamic' https:;
```

# Проверка и отладка CSP
### Проверить CSP в браузере
- В Chrome DevTools → `Security` → `Content Security Policy`
- В `Console` будут ошибки CSP при нарушениях

### Онлайн-проверка CSP
- [Google CSP Evaluator](https://csp-evaluator.withgoogle.com/)
- [Mozilla Observatory](https://observatory.mozilla.org/)

# Итог
`CSP` защищает от [XSS](?General/Abbreviations/Security/XSS), но требует настройки
Используйте `nonce` и `strict-dynamic` вместо `unsafe-inline`
Проверяйте отчёты нарушений (`report-uri`)
Минимально разрешайте источники ресурсов
