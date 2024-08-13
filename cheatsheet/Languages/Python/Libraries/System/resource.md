<p>Библиотека "resource" в Python используется для доступа и управления системными ресурсами, такими как время CPU, память и дескрипторы файлов.</p>
<p>Методы и подмодули модуля "resource":</p>
<p><code>getrusage(who)</code> - возвращает информацию о системных ресурсах для указанного процесса или группы процессов.
<code>getrlimit(resource)</code> - получает текущие ограничения на указанный ресурс.
<code>setrlimit(resource, limits)</code> - устанавливает ограничения на указанный ресурс.
<code>getpagesize()</code> - возвращает размер страницы памяти операционной системы.
<code>getrusage()</code> - возвращает информацию о системных ресурсах для текущего процесса.
<code>RUSAGE_SELF</code> - константа, указывающая на текущий процесс.
<code>RUSAGE_CHILDREN</code> - константа, указывающая на дочерние процессы текущего процесса.</p>
<p>Наиболее часто используемые методы:</p>
<p><code>getrusage(who)</code> - получает информацию о системных ресурсах для указанного процесса или группы процессов.</p>
<pre><code class="language-python">import resource

usage = resource.getrusage(resource.RUSAGE_SELF)
print(usage)
</code></pre>
<p><code>getrlimit(resource)</code> - получает текущие ограничения на указанный ресурс.</p>
<pre><code class="language-python">import resource

limit = resource.getrlimit(resource.RLIMIT_CPU)
print(limit)
</code></pre>
<p><code>setrlimit(resource, limits)</code> - устанавливает ограничения на указанный ресурс.</p>
<pre><code class="language-python">import resource

# Ограничение на время CPU - 2 секунды
limits = (2, resource.RLIM_INFINITY)
resource.setrlimit(resource.RLIMIT_CPU, limits)
</code></pre>