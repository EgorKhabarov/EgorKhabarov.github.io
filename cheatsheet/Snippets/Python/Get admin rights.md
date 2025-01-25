# Windows

```python
import sys
import os
import ctypes


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except:
        return False

# Если скрипт не запущен от имени администратора, перезапускаем его с правами администратора
if not is_admin():
    print("Необходимы права администратора, перезапускаем скрипт...")
    # Перезапуск скрипта с правами администратора
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, ' '.join(sys.argv), None, 1)
    sys.exit(0)

# Ваш код, который требует прав администратора
print("Скрипт запущен с правами администратора!")
```

# Linux / macOS

```python
import os
import sys
import subprocess

# Проверка, запущен ли скрипт с правами администратора
def is_admin():
    return os.geteuid() == 0

# Если скрипт не запущен с правами администратора, перезапускаем его с использованием sudo
if not is_admin():
    print("Необходимы права администратора, перезапускаем скрипт...")
    subprocess.check_call(["sudo", "python3"] + sys.argv)
    sys.exit(0)

# Ваш код, который требует прав администратора
print("Скрипт запущен с правами администратора!")
```
