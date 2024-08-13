<pre><code class="language-bash">pip install tinydb
</code></pre>
<pre><code class="language-python">from tinydb import TinyDB, Query


db = TinyDB(&quot;db.json&quot;)
users_table = db.table(&quot;users&quot;)
user_id = users_table.insert({&quot;name&quot;: &quot;John&quot;, &quot;age&quot;: 25})
all_users = users_table.all()

# Получение записи по условию (например, по имени)
user_query = Query()
john_data = users_table.search(user_query.name == &quot;John&quot;)

# Изменение данных в записи по условию (например, по имени)
users_table.update({&quot;age&quot;: 26}, user_query.name == &quot;John&quot;)

# Удаление записи по условию (например, по имени)
users_table.remove(user_query.name == &quot;John&quot;)
</code></pre>