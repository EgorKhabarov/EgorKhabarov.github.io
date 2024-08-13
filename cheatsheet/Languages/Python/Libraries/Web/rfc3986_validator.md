<p>Название библиотеки: "rfc3986_validator"</p>
<p>Описание: Библиотека "rfc3986_validator" используется для проверки и валидации URL-адресов согласно стандарту RFC 3986.
Она обеспечивает функционал для проверки правильности формата URL и его различных компонентов, таких как схема, хост, путь и другие.</p>
<p>Методы модуля и их описание:</p>
<p>Модуль: rfc3986_validator
validate(url: str) -&gt; bool: Проверяет, соответствует ли заданный URL формату RFC 3986. Возвращает True, если URL действительный, и False в противном случае.
get_scheme(url: str) -&gt; str: Извлекает и возвращает схему (протокол) из заданного URL.
get_host(url: str) -&gt; str: Извлекает и возвращает хост (доменное имя) из заданного URL.
get_path(url: str) -&gt; str: Извлекает и возвращает путь из заданного URL.
get_query(url: str) -&gt; str: Извлекает и возвращает параметры запроса из заданного URL.
get_fragment(url: str) -&gt; str: Извлекает и возвращает фрагмент из заданного URL.</p>
<p>Список самых часто используемых методов, их описание и</p>
<p>validate(url: str) -&gt; bool:
Описание: Проверяет, является ли заданный URL действительным согласно стандарту RFC 3986.</p>
<pre><code class="language-python">from rfc3986_validator import validate

url = &quot;https://www.example.com&quot;
is_valid = validate(url)
print(is_valid)  # Выводит True, если URL действителен
</code></pre>
<p>get_host(url: str) -&gt; str:
Описание: Извлекает и возвращает хост (доменное имя) из заданного URL.</p>
<pre><code class="language-python">from rfc3986_validator import get_host

url = &quot;https://www.example.com/path&quot;
host = get_host(url)
print(host)  # Выводит &quot;www.example.com&quot;
</code></pre>
<p>get_path(url: str) -&gt; str:
Описание: Извлекает и возвращает путь из заданного URL.</p>
<pre><code class="language-python">from rfc3986_validator import get_path

url = &quot;https://www.example.com/path&quot;
path = get_path(url)
print(path)  # Выводит &quot;/path&quot;
</code></pre>