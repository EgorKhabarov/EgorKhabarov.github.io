<p>Библиотека "psutil" в Python используется для доступа и управления информацией о системе и процессах.
Она предоставляет функции для получения информации о процессоре, памяти, дисках, сети и др.
Это полезно для мониторинга системы, оптимизации ресурсов и отладки.</p>
<table>
<thead>
<tr>
<th>Метод</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td>psutil.cpu_percent()</td>
<td>Возвращает процент использования ЦП</td>
</tr>
<tr>
<td>psutil.virtual_memory()</td>
<td>Возвращает информацию о виртуальной памяти</td>
</tr>
<tr>
<td>psutil.disk_usage()</td>
<td>Возвращает использование дискового пространства</td>
</tr>
<tr>
<td>psutil.net_io_counters()</td>
<td>Возвращает сетевые счетчики ввода-вывода</td>
</tr>
<tr>
<td>psutil.process_count()</td>
<td>Возвращает количество запущенных процессов</td>
</tr>
</tbody>
</table>
<p>psutil.cpu_percent(): Возвращает текущий процент использования CPU в виде числа от 0 до 100.</p>
<pre><code class="language-python">import psutil

cpu_percent = psutil.cpu_percent()
print(&quot;Текущий процент использования CPU:&quot;, cpu_percent)
</code></pre>
<p>psutil.virtual_memory(): Возвращает информацию о виртуальной памяти в виде объекта.
Можно получить доступ к атрибутам, таким как "total" (всего памяти), "available" (доступно памяти), "used" (используется памяти) и др.</p>
<pre><code class="language-python">import psutil

virtual_memory = psutil.virtual_memory()
print(&quot;Общая доступная память:&quot;, virtual_memory.total)
print(&quot;Доступная память:&quot;, virtual_memory.available)
print(&quot;Используется памяти:&quot;, virtual_memory.used)
</code></pre>
<p>psutil.disk_usage(): Возвращает информацию об использовании дискового пространства для указанного пути в виде объекта.
Можно получить доступ к атрибутам, таким как "total" (всего пространства),
"used" (используется пространство), "free" (свободное пространство) и др.</p>
<pre><code class="language-python">import psutil

disk_usage = psutil.disk_usage(&quot;/&quot;)
print(&quot;Общее пространство диска:&quot;, disk_usage.total)
print(&quot;Используется пространства диска:&quot;, disk_usage.used)
print(&quot;Свободное пространство диска:&quot;, disk_usage.free)
</code></pre>
<p>psutil.net_io_counters(): Возвращает сетевые счетчики ввода-вывода в виде объекта.
Можно получить доступ к атрибутам, таким как "bytes_sent" (отправленные байты), "bytes_recv" (полученные байты), "packets_sent" (отправленные пакеты) и др.</p>
<pre><code class="language-python">import psutil

net_io_counters = psutil.net_io_counters()
print(&quot;Отправленные байты:&quot;, net_io_counters.bytes_sent)
print(&quot;Полученные байты:&quot;, net_io_counters.bytes_recv)
</code></pre>
<p>psutil.process_count(): Возвращает количество текущих запущенных процессов.</p>
<pre><code class="language-python">import psutil

process_count = psutil.process_count()
print(&quot;Количество запущенных процессов:&quot;, process_count)
</code></pre>