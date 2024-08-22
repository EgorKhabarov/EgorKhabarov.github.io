<p>Команда <code>mkdir</code> используется для создания новой директории.</p>
<p>Флаг <code>/p</code> позволяет создать директорию и ее родительские директории, если они еще не существуют. 
Например:</p>
<div class="code_element"><div class="lang_line"><text>Dockerfile</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-Dockerfile"><div class="highlight"><pre><span></span><span class="k">RUN</span><span class="w"> </span>mkdir<span class="w"> </span>C:<span class="se">\a</span>pp<span class="se">\d</span>ata<span class="se">\l</span>ogs<span class="w"> </span>/p
</pre></div></div></div>

<p>Если же использовать команду <code>RUN mkdir C:\app\data\logs</code> 
и директория <code>C:\app\data</code> еще не существует, то команда <code>mkdir</code> вернет ошибку.</p>