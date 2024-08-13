<pre><code class="language-python">from vedis import Vedis
db = Vedis(&quot;:mem:&quot;)  # Create an in-memory database.
db = Vedis(&quot;Dict.vedis&quot;)
with db.transaction():
    db[&quot;key&quot;] = &quot;value&quot;
    db.rollback()  # Undo changes.
    db.commit()
print(db[&quot;key&quot;])
</code></pre>
<p><a href="https://vedis-python.readthedocs.io/en/latest/quickstart.html">https://vedis-python.readthedocs.io/en/latest/quickstart.html</a></p>
<p>Пример использования в боте
<a href="https://mastergroosha.github.io/telegram-tutorial/docs/lesson_11/">https://mastergroosha.github.io/telegram-tutorial/docs/lesson_11/</a></p>