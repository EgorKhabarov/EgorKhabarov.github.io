<p>Команда <code>mkdir</code> используется для создания новой директории.</p>
<p>Флаг <code>/p</code> позволяет создать директорию и ее родительские директории, если они еще не существуют. 
Например:</p>
<pre><code class="language-Dockerfile">RUN mkdir C:\app\data\logs /p
</code></pre>
<p>Если же использовать команду <code>RUN mkdir C:\app\data\logs</code> 
и директория <code>C:\app\data</code> еще не существует, то команда <code>mkdir</code> вернет ошибку.</p>