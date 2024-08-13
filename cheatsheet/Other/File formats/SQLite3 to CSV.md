<pre><code class="language-python">import sqlite3
import csv

def SQL(query: str, params: tuple | dict = None, commit: bool = False, column_names: bool = False):
    &quot;&quot;&quot;Выполняет SQL запрос&quot;&quot;&quot;
    with sqlite3.connect(r&quot;database.sqlite&quot;) as connection:
        cursor = connection.cursor()
        cursor.execute(query, params)
        if commit: connection.commit()
        result = cursor.fetchall()
        if column_names and getattr(cursor, &quot;description&quot;):
            column_names_data = [column[0] for column in cursor.description] or None
            result = column_names_data + result
    return result

data = SQL(&quot;SELECT * FROM table_name;&quot;)

with open(&quot;data.csv&quot;, &quot;w&quot;, newline=&quot;&quot;, encoding=&quot;UTF-8&quot;) as file:
    writer = csv.writer(file)
    writer.writerows(data)

with open(&quot;data.csv&quot;, &quot;r&quot;, encoding=&quot;UTF-8&quot;) as file:
    reader = csv.reader(file)
    column_names = next(reader)
    SQL(
        f&quot;&quot;&quot;
CREATE TABLE table_name (
    {', '.join([f&quot;{column} TEXT&quot; for column in column_names])}
);
&quot;&quot;&quot;,
        commit=True,
    )
    for row in reader:
        SQL(
            f&quot;&quot;&quot;
INSERT INTO table_name (
    {', '.join(column_names)}
)
VALUES (
    {', '.join([f'&quot;{column}&quot;' for column in row])}
)
&quot;&quot;&quot;,
            commit=True,
        );
</code></pre>