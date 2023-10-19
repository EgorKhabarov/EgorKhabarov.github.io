<p>Библиотека "hmac" в Python используется для создания и проверки кодов аутентификации HMAC (Hash-based Message Authentication Code).
HMAC обеспечивает целостность и аутентификацию сообщений, используя хеш-функции.</p>
<p>Таблица методов модуля "hmac" и их краткого описания:</p>
<table>
<thead>
<tr>
<th>Метод</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td>hmac.new(key, msg, digestmod)</td>
<td>Создает новый объект HMAC с заданным ключом, сообщением и используемой хеш-функцией.</td>
</tr>
<tr>
<td>hmac.digest()</td>
<td>Возвращает HMAC в виде строки байтов.</td>
</tr>
<tr>
<td>hmac.hexdigest()</td>
<td>Возвращает HMAC в виде шестнадцатеричной строки.</td>
</tr>
<tr>
<td>hmac.compare_digest(a, b)</td>
<td>Сравнивает два HMAC без утечек информации о значениях.</td>
</tr>
</tbody>
</table>
<p>(Подмодулей в модуле "hmac" нет)</p>
<p>Список самых часто используемых методов, их краткое описание и</p>
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
<td>hmac.new(key, msg, digestmod)</td>
<td>Создает новый HMAC объект с заданным ключом, сообщением и используемой хеш-функцией.</td>
<td><code>hmac_object = hmac.new(key, msg, hashlib.sha256)</code></td>
</tr>
<tr>
<td>hmac.digest()</td>
<td>Возвращает HMAC в виде строки байтов.</td>
<td><code>hmac_bytes = hmac_object.digest()</code></td>
</tr>
<tr>
<td>hmac.hexdigest()</td>
<td>Возвращает HMAC в виде шестнадцатеричной строки.</td>
<td><code>hmac_string = hmac_object.hexdigest()</code></td>
</tr>
<tr>
<td>hmac.compare_digest(a, b)</td>
<td>Сравнивает два HMAC и возвращает True, если они совпадают, иначе возвращает False.</td>
<td><code>result = hmac.compare_digest(hmac1, hmac2)</code></td>
</tr>
</tbody>
</table>