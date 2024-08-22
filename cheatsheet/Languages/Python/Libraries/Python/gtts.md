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
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">gtts</span> <span class="kn">import</span> <span class="n">gTTS</span>

<span class="n">text</span> <span class="o">=</span> <span class="s2">&quot;Привет, как дела?&quot;</span>
<span class="n">language</span> <span class="o">=</span> <span class="s2">&quot;ru&quot;</span>

<span class="c1"># Создание объекта gTTS с текстом и языком</span>
<span class="n">tts</span> <span class="o">=</span> <span class="n">gTTS</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">text</span><span class="p">,</span> <span class="n">lang</span><span class="o">=</span><span class="n">language</span><span class="p">)</span>

<span class="c1"># Сохранение аудиофайла</span>
<span class="n">tts</span><span class="o">.</span><span class="n">save</span><span class="p">(</span><span class="s2">&quot;output.mp3&quot;</span><span class="p">)</span>

<span class="c1"># Получение списка URL-адресов для визуализации прогресса синтеза речи</span>
<span class="n">urls</span> <span class="o">=</span> <span class="n">tts</span><span class="o">.</span><span class="n">get_urls</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>
</pre></div></div></div>

<p>Эта библиотека полезна для создания аудиофайлов со сгенерированной речью на разных языках.</p>