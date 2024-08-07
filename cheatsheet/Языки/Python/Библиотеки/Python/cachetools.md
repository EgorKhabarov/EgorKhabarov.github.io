<p>Библиотека "cachetools" используется для кэширования в Python.
Он предоставляет различные механизмы кэширования для повышения производительности.
вашего кода, сохраняя и извлекая данные из памяти вместо выполнения
дорогостоящие вычисления или доступ к внешним ресурсам.</p>
<p>Вот таблица, суммирующая основные методы и подмодули модуля «cachetools»:</p>
<table>
<thead>
<tr>
<th>Название</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cache</td>
<td>Основной класс для создания и управления кэшами.</td>
</tr>
<tr>
<td>LRUCache</td>
<td>Реализация кэша, основанная на алгоритме наименее недавно использованного (LRU).</td>
</tr>
<tr>
<td>TTLCache</td>
<td>Реализация кэша с истечением срока жизни (TTL) для кэшированных элементов.</td>
</tr>
<tr>
<td>LFUCache</td>
<td>Реализация кэша, основанная на наименее часто используемом алгоритме (LFU).</td>
</tr>
<tr>
<td>RRCache</td>
<td>Реализация кэша, основанная на алгоритме случайной замены (RR).</td>
</tr>
<tr>
<td>HashedCache</td>
<td>Реализация кэша, использующая хеш-функцию для распределения элементов по нескольким субкэшам.</td>
</tr>
</tbody>
</table>
<p>Вот некоторые из наиболее распространенных методов библиотеки «cachetools»:</p>
<table>
<thead>
<tr>
<th>Название метода</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td>get(key)</td>
<td>Извлекает значение, связанное с указанным ключом, из кэша.</td>
</tr>
<tr>
<td>set(key, value)</td>
<td>Сохраняет значение в кеше с указанным ключом.</td>
</tr>
<tr>
<td>pop(key)</td>
<td>Удаляет элемент с указанным ключом из кэша и возвращает его значение.</td>
</tr>
<tr>
<td>clear()</td>
<td>Очищает все элементы из кэша.</td>
</tr>
<tr>
<td>keys()</td>
<td>Возвращает список всех ключей в кеше.</td>
</tr>
</tbody>
</table>
<p>Вот небольшой фрагмент кода, демонстрирующий использование метода get:</p>
<div class="code-element">
    <div class="lang-line">
        <text>python</text>
        <button class="copy-button"
        onclick="copyCode(this)">
    <svg stroke="currentColor"
         fill="none"
         stroke-width="2"
         viewBox="0 0 24 24"
         stroke-linecap="round"
         stroke-linejoin="round"
         class="h-4 w-4"
         height="1em"
         width="1em"
         xmlns="http://www.w3.org/2000/svg">
        <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
        <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
    </svg>
    <text>Copy code</text>
</button>

    </div>
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">cachetools</span> <span class="kn">import</span> <span class="n">LRUCache</span>

<span class="c1"># Создайте LRUCache с максимальным размером 100</span>
<span class="n">cache</span> <span class="o">=</span> <span class="n">LRUCache</span><span class="p">(</span><span class="n">maxsize</span><span class="o">=</span><span class="mi">100</span><span class="p">)</span>

<span class="c1"># Устанавливаем значение в кеше</span>
<span class="n">cache</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="s2">&quot;key&quot;</span><span class="p">,</span> <span class="s2">&quot;value&quot;</span><span class="p">)</span>

<span class="c1"># Получаем значение из кеша</span>
<span class="n">cached_value</span> <span class="o">=</span> <span class="n">cache</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">&quot;key&quot;</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="n">cached_value</span><span class="p">)</span>  <span class="c1"># &quot;value&quot;</span>
</pre></div></div>
</div>