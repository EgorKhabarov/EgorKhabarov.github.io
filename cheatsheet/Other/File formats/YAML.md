<h1>YAML - Ain't Markup Language</h1>
<p>Формат файлов, который используется для хранения и обмена неструктурированными и структурированными
данными. Например он популярен в файлах настройки приложений, описание конфигураций и т.д.
<code>YAML</code> использует отступы и специальные символы для обозначения структуры данных.
Он также поддерживает множество типов данных, включая строки, числа, логические значения и массивы.</p>
<pre><code class="language-yaml">name: John Smith
age: 30
city: New York
</code></pre>
<pre><code class="language-python">import yaml  # pip install yaml


config = {&quot;BOT&quot;: {&quot;bot_name&quot;: &quot;&quot;, &quot;token&quot;: &quot;&quot;}}

with open(&quot;config.yaml&quot;, &quot;w&quot;, encoding=&quot;utf-8&quot;) as file:
    file.write(yaml.safe_dump(config, sort_keys=False, allow_unicode=True, indent=4))

with open(&quot;config.yaml&quot;, &quot;r&quot;, encoding=&quot;utf-8&quot;) as file:
    config = yaml.safe_load(file.read())

print(config)
</code></pre>