<p>Библиотека "gtts" (Google Text-to-Speech) используется для преобразования текста в речь.
Она предоставляет возможность синтеза голоса на разных языках, используя голосовые данные от Google.</p>
<p>Методы модуля "gtts":
gTTS(text, lang): принимает текст и язык в качестве параметров и возвращает аудиофайл с синтезированным голосом.
save(file): сохраняет аудиофайл на диск.
get_urls(text): возвращает список URL-адресов, которые могут быть использованы для визуализации прогресса синтеза речи.
lang_check(): проверяет доступные языки для синтеза речи.</p>
<p>Методы подмодуля "gtts.lang":
tld(): возвращает список языков и их TLD (top-level domain).
tts_langs(): возвращает список языков, поддерживаемых gTTS.</p>
<p>Самые часто используемые методы:
gTTS(text, lang): Создает объект gTTS с указанным текстом и языком.
save(file): Сохраняет аудиофайл на диск с использованием указанного имени файла и расширения (.mp3).
get_urls(text): Возвращает список URL-адресов для отслеживания прогресса синтеза речи.</p>
<p>Пример кода для использования библиотеки "gtts":</p>
<div class="code-element">
    <div class="lang-line">
        <text>python</text>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">gtts</span> <span class="kn">import</span> <span class="n">gTTS</span>

<span class="n">text</span> <span class="o">=</span> <span class="s2">&quot;Привет, как дела?&quot;</span>
<span class="n">language</span> <span class="o">=</span> <span class="s2">&quot;ru&quot;</span>

<span class="c1"># Создание объекта gTTS с текстом и языком</span>
<span class="n">tts</span> <span class="o">=</span> <span class="n">gTTS</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">lang</span><span class="o">=</span><span class="n">language</span><span class="p">)</span>

<span class="c1"># Сохранение аудиофайла</span>
<span class="n">tts</span><span class="o">.</span><span class="n">save</span><span class="p">(</span><span class="s2">&quot;output.mp3&quot;</span><span class="p">)</span>

<span class="c1"># Получение списка URL-адресов для визуализации прогресса синтеза речи</span>
<span class="n">urls</span> <span class="o">=</span> <span class="n">tts</span><span class="o">.</span><span class="n">get_urls</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>
</pre></div></div>
</div>

<p>Эта библиотека полезна для создания аудиофайлов со сгенерированной речью на разных языках.</p>