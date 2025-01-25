Библиотека "rlcompleter" используется для автоматического завершения кода в интерактивной оболочке Python (REPL) с помощью клавиши Tab.
Она обеспечивает поддержку автозаполнения имён модулей, функций, переменных и атрибутов.

Методы и подмодули библиотеки "rlcompleter":
Submodule: `rlcompleter`
Метод `Completer(...)` - инициализирует объект автозавершения для использования в REPL.
Метод `Completer.complete(text, state)` - выполняет автозавершение указанного текста в заданном состоянии.
Метод `Completer.global_matches(text)` - возвращает список всех глобальных имен, соответствующих указанному тексту.

Метод `Completer.complete(text, state)` - данный метод выполняет автозавершение текста `text` в конкретном состоянии `state`.

```python
import rlcompleter

completer = rlcompleter.Completer()
text = "pr"
state = 0

completions = completer.complete(text, state)
print(completions)
```

Метод `Completer.global_matches(text)` - данный метод возвращает список глобальных имен, которые соответствуют указанному тексту `text`.

```python
import rlcompleter

completer = rlcompleter.Completer()
text = "pr"

matches = completer.global_matches(text)
print(matches)
```
