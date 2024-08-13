<p>Модуль tabnanny в Python используется для проверки исходных файлов
на наличие проблем с табуляцией, которые могут вызвать синтаксические ошибки.</p>
<table>
<thead>
<tr>
<th>Метод</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td>process_tokens(tokens)</td>
<td>Проверяет токены файла на проблемы с табуляцией.</td>
</tr>
<tr>
<td>NannyToken(token)</td>
<td>Конструктор класса токенов, используемый для проверки.</td>
</tr>
</tbody>
</table>
<p><strong>process_tokens(tokens)</strong> Проверяет токены файла на наличие проблем с табуляцией.</p>
<pre><code class="language-python">import tokenize
from tabnanny import process_tokens

with open(&quot;file.py&quot;, &quot;rb&quot;) as f:
    process_tokens(tokenize.generate_tokens(f.readline))
</code></pre>