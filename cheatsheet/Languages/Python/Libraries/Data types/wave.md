Библиотека `wave` используется в Python для работы с аудиофайлами формата WAV
Она позволяет открывать, создавать, записывать и обрабатывать звуковые файлы в формате WAV

|                                      |                                                                 |
|--------------------------------------|-----------------------------------------------------------------|
| `open(file, mode)`                   | Открывает `WAV`-файл с указанным именем файла и режимом доступа |
| `Wave_read.getnchannels()`           | Возвращает число каналов в `WAV`-файле (моно или стерео)        |
| `Wave_read.getsampwidth()`           | Возвращает размер образца в байтах                              |
| `Wave_read.getframerate()`           | Возвращает частоту дискретизации аудиофайла                     |
| `Wave_read.getnframes()`             | Возвращает количество фреймов в аудиофайле                      |
| `Wave_read.readframes(n)`            | Читает и возвращает `n` фреймов из аудиофайла                   |
| `Wave_write.setnchannels(nchannels)` | Устанавливает число каналов для нового `WAV`-файла              |
| `Wave_write.setsampwidth(sampwidth)` | Устанавливает размер образца для нового `WAV`-файла             |
| `Wave_write.setframerate(framerate)` | Устанавливает частоту дискретизации для нового `WAV`-файла      |
| `Wave_write.writeframesraw(data)`    | Записывает сырые байты аудио-данных в новый `WAV`-файл          |
| `Wave_write.writeframes(data)`       | Записывает фреймы аудио-данных в новый `WAV`-файл               |

#### open(file, mode)
Открывает WAV-файл для чтения или записи

```python
import wave

with wave.open("audio.wav", "r") as wav_file:
    pass  # проведите необходимые операции с аудиофайлом
```

### Wave_read.getnframes()
Возвращает количество фреймов в аудиофайле

```python
import wave

with wave.open("audio.wav", "r") as wav_file:
    num_frames = wav_file.getnframes()
    print(f"Number of frames: {num_frames}")
```

### Wave_write.writeframes(data)
Записывает фреймы аудио-данных в новый WAV-файл

```python
import wave

new_frames = b"\x00\x00\x00\x00\x00\x00\x00\x00"  # пример сырых байтов аудио-данных

with wave.open("new_audio.wav", "w") as wav_file:
    wav_file.setnchannels(1)  # устанавливаем один канал
    wav_file.setsampwidth(2)  # устанавливаем размер образца в два байта
    wav_file.setframerate(44100)  # устанавливаем частоту дискретизации в 44100 Гц
    wav_file.writeframes(new_frames)  # записываем фреймы в новый WAV-файл
```
