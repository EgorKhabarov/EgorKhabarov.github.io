<h1>INI (Initialization)</h1>
<p>формат конфигурационных файлов, который используется 
для хранения настроек приложений и операционных систем. 
Он был разработан в <code>Windows</code> и стал широко используемым 
форматом для хранения конфигурационных данных в различных программных продуктах.</p>
<pre><code class="language-ini">[Section1]
key1 = value1
key2 = value2

[Section2]
key3 = value3
key4 = value4
</code></pre>
<pre><code class="language-python"># config = configparser.ConfigParser()
# config[&quot;BOT&quot;] = {&quot;bot_name&quot;: &quot;&quot;, &quot;token&quot;: &quot;&quot;}

import configparser


config = {&quot;BOT&quot;: {&quot;bot_name&quot;: &quot;&quot;, &quot;token&quot;: &quot;&quot;}}
config_ini = configparser.ConfigParser()

for key, value in config.items():
    config_ini[key] = value

with open(&quot;config.ini&quot;, &quot;w&quot;) as file:
    config_ini.write(file)

config_ini = configparser.ConfigParser()
config_ini.read(&quot;config.ini&quot;)
print(config)
</code></pre>