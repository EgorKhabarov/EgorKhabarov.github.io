<h1>CSV - Comma Separated Values</h1>
<p>Текстовый формат файла, который используется для хранения табличных данных.
Каждая строка файла содержит одну запись, а значения в этой записи разделены запятыми.</p>
<pre><code class="language-csv">Name,Age,City
John Smith,30,New York
Jane Doe,25,Chicago
</code></pre>
<pre><code class="language-python">import csv


data = [
    (&quot;Name&quot;, &quot;Age&quot;),
    (&quot;Alice&quot;, 25),
    (&quot;Bob&quot;, 30),
    (&quot;Charlie&quot;, 35),
]

with open(&quot;data.csv&quot;, &quot;w&quot;, newline=&quot;&quot;, encoding=&quot;UTF-8&quot;) as file:
    csv.writer(file).writerows(data)

with open(&quot;data.csv&quot;, &quot;r&quot;, encoding=&quot;UTF-8&quot;) as file:
    print(list(csv.reader(file)))
</code></pre>