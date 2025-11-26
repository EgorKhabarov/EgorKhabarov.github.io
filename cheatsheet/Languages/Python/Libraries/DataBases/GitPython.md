# GitPython

**`GitPython`** библиотека для управления Git-репозиториями в Python
Позволяет выполнять команды Git, работать с коммитами, ветками, файлами и историей

## Установка
```sh
pip install gitpython
```

## Основные классы
| Класс        | Описание                                 |
|--------------|------------------------------------------|
| `git.Repo`   | Основной класс для работы с репозиторием |
| `git.Commit` | Представляет коммит                      |
| `git.Tree`   | Представляет дерево файлов               |
| `git.Index`  | Отвечает за индекс (staging area)        |
| `git.Remote` | Представляет удаленный репозиторий       |
| `git.Head`   | Ветка (указатель на коммит)              |
| `git.Tag`    | Тег                                      |
| `git.Diff`   | Различия между версиями                  |
| `git.Blob`   | Файлы в репозитории                      |

# Работа с репозиториями

## Открытие репозитория
```python
import git

repo = git.Repo("/путь/к/репозиторию")  # Открывает существующий репозиторий
print(repo.git_dir)  # Выводит путь к .git
```

## Клонирование репозитория
```python
repo = git.Repo.clone_from("https://github.com/user/repo.git", "/путь/к/папке")
```

## Создание нового репозитория
```python
repo = git.Repo.init("/путь/к/новому/репозиторию")
```

# Работа с коммитами

## Получение текущего коммита
```python
commit = repo.head.commit
print(commit.hexsha)  # Хеш коммита
print(commit.message)  # Сообщение коммита
print(commit.author)   # Автор
print(commit.committed_datetime)  # Дата коммита
```

## История коммитов
```python
for commit in repo.iter_commits():
    print(commit.hexsha, commit.message)
```

## Создание коммита
```python
repo.index.add(["file.txt"])  # Добавление файла в индекс
repo.index.commit("Мое сообщение коммита")  # Создание коммита
```

# Работа с ветками

## Получение текущей ветки
```python
print(repo.active_branch)
```

## Создание новой ветки
```python
repo.git.branch("новая_ветка")
```

## Переключение на ветку
```python
repo.git.checkout("новая_ветка")
```

## Удаление ветки
```python
repo.git.branch("-d", "новая_ветка")
```

# Работа с удаленными репозиториями

## Получение удаленных репозиториев
```python
for remote in repo.remotes:
    print(remote.name, remote.url)
```

## Добавление удаленного репозитория
```python
origin = repo.create_remote("origin", "https://github.com/user/repo.git")
```

## Удаление удаленного репозитория
```python
repo.delete_remote("origin")
```

## Получение изменений с удаленного репозитория
```python
repo.remotes.origin.fetch()
```

## Отправка изменений
```python
repo.remotes.origin.push()
```

# Разница между версиями

## Получение различий
```python
diff = repo.head.commit.diff("HEAD~1")  # Разница с предыдущим коммитом
for change in diff:
    print(change.a_path, "→", change.b_path)
```

# Вспомогательные команды

## Проверка статуса
```python
print(repo.git.status())
```

## Список файлов в индексе
```python
print(repo.index.entries.keys())
```

## Получение логов
```python
print(repo.git.log("--oneline"))
```
