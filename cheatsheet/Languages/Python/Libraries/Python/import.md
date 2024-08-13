<pre><code class="language-pycon">&gt;&gt;&gt; def im():
...     import math
...
&gt;&gt;&gt; math
Traceback (most recent call last):
  File &quot;&lt;stdin&gt;&quot;, line 1, in &lt;module&gt;
NameError: name 'math' is not defined
&gt;&gt;&gt; im()
&gt;&gt;&gt; math
Traceback (most recent call last):
  File &quot;&lt;stdin&gt;&quot;, line 1, in &lt;module&gt;
NameError: name 'math' is not defined
</code></pre>
<pre><code class="language-python">import importlib

importlib.reload(my_module)
</code></pre>
<pre><code class="language-python">import subprocess
import importlib

library_name = input(&quot;Введите название библиотеки, которую вы хотите установить: &quot;)

# проверяем, установлена ли библиотека
try:
    importlib.import_module(library_name)
    print(f&quot;Библиотека {library_name} уже установлена.&quot;)
except ImportError:
    # устанавливаем библиотеку
    subprocess.call([&quot;pip&quot;, &quot;install&quot;, library_name])
    print(f&quot;Библиотека {library_name} установлена успешно.&quot;)

</code></pre>