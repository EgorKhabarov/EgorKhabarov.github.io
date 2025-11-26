

`llm.txt` (или `llms.txt`) новая, экспериментальная практика, появившаяся в 2023–2024 годах,
предназначенная для управления доступом **AI-агентов (в основном LLM)** к контенту сайтов, по аналогии с [[General/HTTP/robots.txt]]

## Что такое `llm.txt` / `llms.txt`

Файл `llm.txt` или `llms.txt` **новый механизм**, позволяющий **владельцам сайтов указать, могут ли большие языковые модели (LLMs)**, такие как GPT, Claude, Gemini и др., **использовать контент сайта для обучения, ответов и анализа**

- `https://example.com/llm.txt`
- или (альтернативно) `https://example.com/llms.txt`

## Цель файла

- Аналог `robots.txt`, но **для LLM-агентов**, а не поисковых роботов
- Предоставляет возможность **разрешить или запретить** доступ конкретным LLM-платформам
- Используется для **регулирования использования контента** в генеративных AI-сервисах (например, ChatGPT, Perplexity, Claude и пр.)

## Синтаксис и структура

На момент 2025 года **не существует стандартизированного формата**, но де-факто принят следующий

```
User-agent: <название модели или сервиса>
Disallow: <путь>  # Запрещает доступ
Allow: <путь>     # Разрешает доступ
```

Также может встречаться

- `Disallow: /` полный запрет
- `#` комментарии
- Wildcard-поддержка не гарантируется, но может быть распознана

## Примеры

### Запретить всем LLM

```txt
User-agent: *
Disallow: /
```

### Запретить GPT и Claude, разрешить другим

```txt
User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /
```

### Разрешить всё GPTBot и Claude

```txt
User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /
```

### Разрешить GPTBot только на /blog/

```txt
User-agent: GPTBot
Disallow: /
Allow: /blog/
```

## Наиболее известные LLM-боты и их `User-agent`'ы

| Модель / сервис      | User-agent                 |
|----------------------|----------------------------|
| **OpenAI GPTBot**    | `GPTBot`                   |
| **Anthropic Claude** | `ClaudeBot`                |
| **Google Gemini**    | `Google-Extended`          |
| **Perplexity AI**    | `PerplexityBot`            |
| **You.com**          | `YouBot`                   |
| **Meta**             | `MetaBot` *(спекулятивно)* |

*Важно: список пополняется. Названия user-agent’ов нужно уточнять у каждой платформы.*

## Ограничения и нюансы

- **Никакая платформа не обязана соблюдать `llm.txt`**, если только она **добровольно это не делает**
- Некоторые боты (например, GPTBot и ClaudeBot) **официально уважают файл**
- Это **новая и развивающаяся практика**, не закреплённая в стандартах IETF/W3C
- `llm.txt` - **не защита**, а просьба. Для настоящей защиты - технические меры (CAPTCHA, токены, paywall)

## Технические меры в дополнение

Чтобы действительно **защитить контент** от LLM и скраперов

| Мера                        | Примечание                                        |
|-----------------------------|---------------------------------------------------|
| `robots.txt` + `llm.txt`    | Декларативное регулирование                       |
| `robots` meta-тег           | `<meta name="robots" content="noindex,nofollow">` |
| `X-Robots-Tag` в заголовках | Тоже может указывать noindex                      |
| Блокировка IP-диапазонов    | Уточняется в документации GPTBot и других         |
| User-Agent фильтрация       | Веб-сервер может блокировать известных ботов      |
| Captcha / JS-чек            | Помогает против автоматизированного сбора         |

## Как узнать, кто использует мой сайт

Используй логи доступа веб-сервера, ищи `User-Agent`, например

```
GPTBot
ClaudeBot
PerplexityBot
Google-Extended
```

Или установи аналитические инструменты (например, WAF, логеры NGINX/Apache)

## Ссылки на официальные страницы LLM-ботов

- **OpenAI GPTBot**: [https://openai.com/gptbot](https://openai.com/gptbot)
- **Anthropic ClaudeBot**: [https://www.anthropic.com/claudebot](https://www.anthropic.com/claudebot)
- **Google-Extended** (Gemini): [https://developers.google.com/search/docs/crawling-indexing/googlebot#google-extended](https://developers.google.com/search/docs/crawling-indexing/googlebot#google-extended)
- **PerplexityBot**: [https://www.perplexity.ai/blog/perplexitybot](https://www.perplexity.ai/blog/perplexitybot)
- **YouBot**: *(официальной страницы может не быть)*

## Пример `llm.txt` для сайта

```txt
# Ограничения для LLM-ботов
User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /

User-agent: PerplexityBot
Disallow: /

User-agent: *
Disallow: /private/
Allow: /
```

## Заключение

Файл `llm.txt` - это **новый и добровольный механизм**, позволяющий выразить позицию владельца сайта по поводу использования его контента ИИ-моделями
Но пока нет единого стандарта, и соблюдение зависит от доброй воли разработчиков LLM

