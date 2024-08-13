<p>Библиотека "rlcompleter" используется для автоматического завершения кода в интерактивной оболочке Python (REPL) с помощью клавиши Tab.
Она обеспечивает поддержку автозаполнения имён модулей, функций, переменных и атрибутов.</p>
<p>Методы и подмодули библиотеки "rlcompleter":
Submodule: <code>rlcompleter</code>
Метод <code>Completer(...)</code> - инициализирует объект автозавершения для использования в REPL.
Метод <code>Completer.complete(text, state)</code> - выполняет автозавершение указанного текста в заданном состоянии.
Метод <code>Completer.global_matches(text)</code> - возвращает список всех глобальных имен, соответствующих указанному тексту.</p>
<p>Метод <code>Completer.complete(text, state)</code> - данный метод выполняет автозавершение текста <code>text</code> в конкретном состоянии <code>state</code>.</p>
<pre><code class="language-python">import rlcompleter

completer = rlcompleter.Completer()
text = &quot;pr&quot;
state = 0

completions = completer.complete(text, state)
print(completions)
</code></pre>
<p>Метод <code>Completer.global_matches(text)</code> - данный метод возвращает список глобальных имен, которые соответствуют указанному тексту <code>text</code>.</p>
<pre><code class="language-python">import rlcompleter

completer = rlcompleter.Completer()
text = &quot;pr&quot;

matches = completer.global_matches(text)
print(matches)
</code></pre>