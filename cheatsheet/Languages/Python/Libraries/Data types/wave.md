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
<pre><code class="language-python">import wave

with wave.open(&quot;audio.wav&quot;, &quot;r&quot;) as wav_file:
    # проведите необходимые операции с аудиофайлом
</code></pre>
<p>wave.Wave_read.getnframes(): Возвращает количество фреймов в аудиофайле.</p>
<pre><code class="language-python">import wave

with wave.open(&quot;audio.wav&quot;, &quot;r&quot;) as wav_file:
    num_frames = wav_file.getnframes()
    print(f&quot;Number of frames: {num_frames}&quot;)
</code></pre>
<p>wave.Wave_write.writeframes(data): Записывает фреймы аудио-данных в новый WAV-файл.</p>
<pre><code class="language-python">import wave

new_frames = b&quot;\x00\x00\x00\x00\x00\x00\x00\x00&quot;  # пример сырых байтов аудио-данных

with wave.open(&quot;new_audio.wav&quot;, &quot;w&quot;) as wav_file:
    wav_file.setnchannels(1)  # устанавливаем один канал
    wav_file.setsampwidth(2)  # устанавливаем размер образца в два байта
    wav_file.setframerate(44100)  # устанавливаем частоту дискретизации в 44100 Гц
    wav_file.writeframes(new_frames)  # записываем фреймы в новый WAV-файл
</code></pre>