<h1>JSON - JavaScript Object Notation</h1>
<p>Tекстовый формат обмена данными, который основан на синтаксисе JavaScript.
Он используется для хранения и обмена структурированными данными и часто используется
в веб-приложениях для обмена данными между клиентом и сервером.</p>
<pre><code class="language-json">{
    &quot;name&quot;: &quot;John Smith&quot;,
    &quot;age&quot;: 30,
    &quot;city&quot;: &quot;New York&quot;
}
</code></pre>
<pre><code class="language-python">import json


config = {&quot;BOT&quot;: {&quot;bot_name&quot;: &quot;&quot;, &quot;token&quot;: &quot;&quot;}}

with open(&quot;config.json&quot;, &quot;w&quot;, encoding=&quot;UTF-8&quot;) as file:
    file.write(json.dumps(config, indent=4, ensure_ascii=False))
    # json.dump(config, file, indent=4, ensure_ascii=False)

with open(&quot;config.json&quot;, &quot;r&quot;, encoding=&quot;UTF-8&quot;) as file:
    config = json.load(file)
    # config = json.loads(file.read())

print(config)
</code></pre>
<h1>JSONL</h1>
<pre><code class="language-python">{&quot;name&quot;: &quot;Alice Jones&quot;, &quot;age&quot;: 25, &quot;city&quot;: &quot;Los Angeles&quot;}
{&quot;name&quot;: &quot;John Smith&quot;, &quot;age&quot;: 30, &quot;city&quot;: &quot;New York&quot;}
{&quot;name&quot;: &quot;Bob Johnson&quot;, &quot;age&quot;: 40, &quot;city&quot;: &quot;Chicago&quot;}
</code></pre>
<pre><code class="language-python">import json


config = [
    {&quot;name&quot;: &quot;Alice Jones&quot;, &quot;age&quot;: 25, &quot;city&quot;: &quot;Los Angeles&quot;},
    {&quot;name&quot;: &quot;John Smith&quot;, &quot;age&quot;: 30, &quot;city&quot;: &quot;New York&quot;},
    {&quot;name&quot;: &quot;Bob Johnson&quot;, &quot;age&quot;: 40, &quot;city&quot;: &quot;Chicago&quot;},
]

with open(&quot;test.jsonl&quot;, &quot;a&quot;, encoding=&quot;UTF-8&quot;) as file:
    file.writelines([str(line) + &quot;\n&quot; for line in config])

with open(&quot;config.jsonl&quot;, &quot;r&quot;, encoding=&quot;UTF-8&quot;) as file:
    for line in file:
        print(json.loads(line))
</code></pre>
<p><a target="_self" href="./?Other/Форматы файлов/TinyDB (json).md">TinyDB (json)</a></p>