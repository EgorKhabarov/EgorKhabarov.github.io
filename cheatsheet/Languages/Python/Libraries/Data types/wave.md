<p>Библиотека "wave" используется в Python для работы с аудиофайлами формата WAV.
Она позволяет открывать,
создавать, записывать и обрабатывать звуковые файлы в формате WAV.
Методы и подмодули библиотеки "wave" и их краткое описание:</p>
<p>wave.open(file, mode): Открывает WAV-файл с указанным именем файла и режимом доступа.
wave.Wave_read.getnchannels(): Возвращает число каналов в WAV-файле (моно или стерео).
wave.Wave_read.getsampwidth(): Возвращает размер образца в байтах.
wave.Wave_read.getframerate(): Возвращает частоту дискретизации аудиофайла.
wave.Wave_read.getnframes(): Возвращает количество фреймов в аудиофайле.
wave.Wave_read.readframes(n): Читает и возвращает n фреймов из аудиофайла.
wave.Wave_write.setnchannels(nchannels): Устанавливает число каналов для нового WAV-файла.
wave.Wave_write.setsampwidth(sampwidth): Устанавливает размер образца для нового WAV-файла.
wave.Wave_write.setframerate(framerate): Устанавливает частоту дискретизации для нового WAV-файла.
wave.Wave_write.writeframesraw(data): Записывает сырые байты аудио-данных в новый WAV-файл.
wave.Wave_write.writeframes(data): Записывает фреймы аудио-данных в новый WAV-файл.</p>
<p>wave.open(file, mode): Открывает WAV-файл для чтения или записи.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">wave</span>

<span class="k">with</span> <span class="n">wave</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s2">&quot;audio.wav&quot;</span><span class="p">,</span> <span class="s2">&quot;r&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">wav_file</span><span class="p">:</span>
    <span class="c1"># проведите необходимые операции с аудиофайлом</span>
</pre></div></div></div>

<p>wave.Wave_read.getnframes(): Возвращает количество фреймов в аудиофайле.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">wave</span>

<span class="k">with</span> <span class="n">wave</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s2">&quot;audio.wav&quot;</span><span class="p">,</span> <span class="s2">&quot;r&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">wav_file</span><span class="p">:</span>
    <span class="n">num_frames</span> <span class="o">=</span> <span class="n">wav_file</span><span class="o">.</span><span class="n">getnframes</span><span class="p">()</span>
    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Number of frames: </span><span class="si">{</span><span class="n">num_frames</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p>wave.Wave_write.writeframes(data): Записывает фреймы аудио-данных в новый WAV-файл.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">wave</span>

<span class="n">new_frames</span> <span class="o">=</span> <span class="sa">b</span><span class="s2">&quot;</span><span class="se">\x00\x00\x00\x00\x00\x00\x00\x00</span><span class="s2">&quot;</span>  <span class="c1"># пример сырых байтов аудио-данных</span>

<span class="k">with</span> <span class="n">wave</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s2">&quot;new_audio.wav&quot;</span><span class="p">,</span> <span class="s2">&quot;w&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">wav_file</span><span class="p">:</span>
    <span class="n">wav_file</span><span class="o">.</span><span class="n">setnchannels</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>  <span class="c1"># устанавливаем один канал</span>
    <span class="n">wav_file</span><span class="o">.</span><span class="n">setsampwidth</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>  <span class="c1"># устанавливаем размер образца в два байта</span>
    <span class="n">wav_file</span><span class="o">.</span><span class="n">setframerate</span><span class="p">(</span><span class="mi">44100</span><span class="p">)</span>  <span class="c1"># устанавливаем частоту дискретизации в 44100 Гц</span>
    <span class="n">wav_file</span><span class="o">.</span><span class="n">writeframes</span><span class="p">(</span><span class="n">new_frames</span><span class="p">)</span>  <span class="c1"># записываем фреймы в новый WAV-файл</span>
</pre></div></div></div>