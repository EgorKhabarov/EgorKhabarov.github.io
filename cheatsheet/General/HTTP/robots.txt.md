# robots.txt

`robots.txt` - это текстовый файл, размещаемый в корне сайта, который сообщает поисковым роботам (краулерам),
какие страницы или разделы сайта можно или нельзя индексировать

`/robots.txt`

Файл состоит из одного или нескольких блоков правил, каждый начинается с `User-Agent`

```
User-Agent: <имя бота>
Allow: <путь>
Disallow: <путь>
Crawl-Delay: <секунды>
Sitemap: <URL карты сайта>
```

# Директивы

- `User-Agent` - указывает, к какому боту применяются правила
- `Allow` - путь, который **можно** индексировать (даже если он входит в запрещённый каталог)
- `Disallow` - путь, который **нельзя** индексировать
- `Crawl-Delay` - задержка между запросами (в секундах)
- `Sitemap` - ссылка на XML-карту сайта

## Особенности и поведение

| Особенность    | Описание                                                                              |
|----------------|---------------------------------------------------------------------------------------|
| Регистр        | Все директивы нечувствительны к регистру, но пути чувствительны (`/Admin` ≠ `/admin`) |
| Wildcard       | Поддерживаются `*` и `$` (не всеми ботами)                                            |
| Комментарии    | Строки, начинающиеся с `#`, игнорируются                                              |
| Порядок правил | Важно для некоторых ботов (например, Google: самое точное правило применяется)        |

## Wildcard (шаблоны путей)

| Символ | Значение                          |
|--------|-----------------------------------|
| `*`    | Любая последовательность символов |
| `$`    | Конец строки                      |

```txt
Disallow: /*.pdf$    # Запретить все PDF
Allow: /public/*     # Разрешить все в /public/
Disallow: /private/  # Запретить всё в /private/
```

## User-Agent

- `*` - правило применяется ко **всем** роботам
- Конкретное имя - только для указанного бота (например, `Googlebot`, `Bingbot`)

```txt
User-Agent: Googlebot
Disallow: /no-google/

User-Agent: *
Disallow: /no-all/
```

## Sitemap

Рекомендуется указывать ссылку на карту сайта (XML)

```txt
Sitemap: https://example.com/sitemap.xml
```

Можно указывать несколько карт

```txt
Sitemap: https://example.com/sitemap1.xml
Sitemap: https://example.com/sitemap2.xml
```

## Crawl-Delay

Ограничивает частоту запросов от бота (не поддерживается Googlebot)

```txt
User-Agent: bingbot
Crawl-Delay: 10  # 10 секунд между запросами
```

# Частые ошибки

| Ошибка                 | Почему плохо                                                        |
|------------------------|---------------------------------------------------------------------|
| `Disallow: /`          | Запретит индексацию **всего сайта**                                 |
| `robots.txt` ≠ UTF-8   | Боты могут не понять                                                |
| Путь без `/`           | Всегда должен начинаться с `/`                                      |
| Переопределение правил | Последовательность `Allow` и `Disallow` должна быть точной          |
| Ожидание безопасности  | `robots.txt` - лишь рекомендация, злоумышленники могут игнорировать |

# Примеры

### Разрешить всё всем

```txt
User-Agent: *
Disallow:
```

### Запретить всё всем

```txt
User-Agent: *
Disallow: /
```

### Разрешить всё, кроме /admin/

```txt
User-Agent: *
Disallow: /admin/
```

### Запретить только PDF-файлы

```txt
User-Agent: *
Disallow: /*.pdf$
```

### Только Googlebot не может индексировать /tmp

```txt
User-Agent: Googlebot
Disallow: /tmp/
```

### Запрет на доступ к параметрам URL

```txt
User-Agent: *
Disallow: /*?sessionid=
Disallow: /*.php$
```

### Запрет на весь каталог, но разрешение для отдельного файла

```txt
User-Agent: *
Disallow: /docs/
Allow: /docs/readme.html
```

# Проверка и отладка

- Google Search Console: Инструмент "Проверка robots.txt"
- Онлайн-валидаторы: [https://technicalseo.com/tools/robots-txt/](https://technicalseo.com/tools/robots-txt/)

# Важное о безопасности

- `robots.txt` - **не защита**, а рекомендация
- Не размещайте **чувствительные пути** (например, `/private-data/`) - они могут быть легко найдены
- Для настоящей защиты используйте HTTP-аутентификацию, `.htaccess`, заголовки `X-Robots-Tag`, или Meta-теги

# Расширения и альтернативы

- **Meta robots tag**: На уровне страницы (`<meta name="robots" content="noindex, nofollow">`)
- **X-Robots-Tag**: В HTTP-заголовках
- Используется совместно с `robots.txt` для более точного контроля

# Ссылки на официальную документацию

- [Google: robots.txt спецификация](https://developers.google.com/search/docs/crawling-indexing/robots/intro)
- [Yandex: robots.txt](https://yandex.ru/support/webmaster/robot-workings/robots-txt.html)
- [Sitemaps.org: Sitemap directive](https://www.sitemaps.org/protocol.html)
