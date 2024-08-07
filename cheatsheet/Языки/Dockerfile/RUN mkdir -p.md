<p>Команда <code>mkdir</code> используется для создания новой директории.</p>
<p>Флаг <code>/p</code> позволяет создать директорию и ее родительские директории, если они еще не существуют. 
Например:</p>
<div class="code-element">
    <div class="lang-line">
        <text>Dockerfile</text>
        <button class="copy-button"
        onclick="copyCode(this)">
    <svg stroke="currentColor"
         fill="none"
         stroke-width="2"
         viewBox="0 0 24 24"
         stroke-linecap="round"
         stroke-linejoin="round"
         class="h-4 w-4"
         height="1em"
         width="1em"
         xmlns="http://www.w3.org/2000/svg">
        <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
        <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
    </svg>
    <text>Copy code</text>
</button>

    </div>
    <div class="code"><div class="highlight"><pre><span></span><span class="k">RUN</span><span class="w"> </span>mkdir<span class="w"> </span>C:<span class="se">\a</span>pp<span class="se">\d</span>ata<span class="se">\l</span>ogs<span class="w"> </span>/p
</pre></div></div>
</div>

<p>Если же использовать команду <code>RUN mkdir C:\app\data\logs</code> 
и директория <code>C:\app\data</code> еще не существует, то команда <code>mkdir</code> вернет ошибку.</p>