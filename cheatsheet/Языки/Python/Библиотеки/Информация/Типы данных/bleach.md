<p>Библиотека "bleach" используется для безопасного удаления или экранирования HTML-тегов и атрибутов в тексте,
чтобы предотвратить возможность внедрения вредоносного кода или XSS-атак.</p>
<table>
<thead>
<tr>
<th>Метод</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td>clean</td>
<td>Удаляет или экранирует HTML-теги и атрибуты из текста</td>
</tr>
<tr>
<td>linkify</td>
<td>Преобразует URL-адреса в тексте в ссылки</td>
</tr>
<tr>
<td>strip_tags</td>
<td>Удаляет все HTML-теги из текста</td>
</tr>
<tr>
<td>escape</td>
<td>Экранирует HTML-сущности в тексте</td>
</tr>
<tr>
<td>unescape</td>
<td>Преобразует экранированные HTML-сущности в их исходное состояние</td>
</tr>
</tbody>
</table>
<p>Наиболее часто используемые методы "bleach" вместе с их кратким описанием и примером кода:</p>
<table>
<thead>
<tr>
<th>Метод</th>
<th>Описание</th>
<th>Пример кода</th>
</tr>
</thead>
<tbody>
<tr>
<td>clean</td>
<td>Удаляет или экранирует HTML-теги и атрибуты</td>
<td>clean(text, tags=["p", "a"])</td>
</tr>
<tr>
<td>linkify</td>
<td>Преобразует URL-адреса в тексте в ссылки</td>
<td>linkify(text)</td>
</tr>
<tr>
<td>strip_tags</td>
<td>Удаляет все HTML-теги из текста</td>
<td>strip_tags(text)</td>
</tr>
<tr>
<td>escape</td>
<td>Экранирует HTML-сущности в тексте</td>
<td>escape(text)</td>
</tr>
<tr>
<td>unescape</td>
<td>Преобразует экранированные HTML-сущности</td>
<td>unescape(text)</td>
</tr>
</tbody>
</table>