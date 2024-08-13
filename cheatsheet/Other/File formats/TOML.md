<h1>TOML - Tom's Obvious, Minimal Language</h1>
<p>формат конфигурационных файлов, который был разработан
для использования в проектах, написанных на языке программирования <code>Rust</code>.</p>
<p>TOML файлы имеют структуру ключ-значение, где ключи и значения
разделены знаком <code>=</code>, и используют синтаксис, похожий на язык программирования <code>INI</code>.</p>
<pre><code class="language-toml">[package]
name = &quot;example&quot;
version = &quot;1.0.0&quot;
authors = [&quot;John Doe &lt;john@example.com&gt;&quot;]
</code></pre>
<pre><code class="language-python">import toml  # pip install toml


config = {&quot;BOT&quot;: {&quot;bot_name&quot;: &quot;&quot;, &quot;token&quot;: &quot;&quot;}}

with open(&quot;config.toml&quot;, &quot;w&quot;, encoding=&quot;UTF-8&quot;) as file:
    file.write(toml.dumps(config))
    # toml.dump(config, file)

with open(&quot;config.toml&quot;, &quot;r&quot;, encoding=&quot;UTF-8&quot;) as file:
    config = toml.load(file)
    # config = toml.loads(file.read())

print(config)
</code></pre>