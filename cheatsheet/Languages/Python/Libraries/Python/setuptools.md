<table>
<thead>
<tr>
<th>Метод</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td>setup()</td>
<td>Определяет настройки проекта и его зависимости.</td>
</tr>
<tr>
<td>find_packages()</td>
<td>Автоматически находит и включает все пакеты проекта.</td>
</tr>
<tr>
<td>find_namespace_packages()</td>
<td>Аналогично find_packages(), но для пространств имен.</td>
</tr>
<tr>
<td>setup_requires</td>
<td>Зависимости, необходимые для установки проекта.</td>
</tr>
<tr>
<td>install_requires</td>
<td>Зависимости, необходимые для работы проекта.</td>
</tr>
<tr>
<td>entry_points</td>
<td>Позволяет определить точки входа (entry points) для проекта.</td>
</tr>
</tbody>
</table>
<p><strong>setup()</strong></p>
<p>Описание: Определяет основные настройки проекта и его зависимости.</p>
<pre><code class="language-python">from setuptools import setup

setup(
    name=&quot;mypackage&quot;,
    version=&quot;1.0.0&quot;,
    packages=[&quot;mypackage&quot;],
    install_requires=[&quot;requests&quot;],
)
</code></pre>
<p><strong>find_packages()</strong></p>
<p>Описание: Автоматически находит и включает все пакеты проекта.</p>
<pre><code class="language-python">from setuptools import setup, find_packages

setup(
    name=&quot;mypackage&quot;,
    version=&quot;1.0.0&quot;,
    packages=find_packages(),
)
</code></pre>
<p><strong>entry_points</strong></p>
<p>Описание: Позволяет определить точки входа (entry points) для проекта, например, для создания скриптов командной строки.</p>
<pre><code class="language-python">from setuptools import setup

setup(
    name=&quot;mypackage&quot;,
    version=&quot;1.0.0&quot;,
    entry_points={
        &quot;console_scripts&quot;: [
            &quot;myscript = mypackage.script:main&quot;,
        ],
    },
)
</code></pre>