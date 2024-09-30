<h2><strong><code>unittest.mock</code></strong>: имитация объектов</h2>
<p><strong><code>unittest.mock</code></strong> — это мощная библиотека, встроенная в <code>unittest</code>, для замены объектов в ваших тестах.
Она позволяет подменять зависимости, чтобы изолировать тестируемый код от внешних систем
(например, базы данных, веб-сервисы, файлы) и тестировать логику в более контролируемой среде.</p>
<h3>Основные компоненты</h3>
<table>
<thead>
<tr>
<th>Компонент</th>
<th>Описание</th>
<th>Пример использования</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Mock()</code></td>
<td>Создает имитацию объекта (mock),<br>который можно настраивать, как угодно</td>
<td><code>mock_obj = Mock()</code></td>
</tr>
<tr>
<td><code>patch()</code></td>
<td>Контекстный менеджер или декоратор для замены объектов<br>(например, функций или классов) на mock во время тестов</td>
<td><code>with patch("module.ClassName") as MockClass: ...</code></td>
</tr>
<tr>
<td><code>assert_called()</code></td>
<td>Проверяет, был ли вызван mock</td>
<td><code>mock_obj.assert_called()</code></td>
</tr>
<tr>
<td><code>assert_called_once()</code></td>
<td>Проверяет, что mock был вызван ровно один раз</td>
<td><code>mock_obj.assert_called_once()</code></td>
</tr>
<tr>
<td><code>assert_called_with()</code></td>
<td>Проверяет, что mock был вызван с определенными аргументами</td>
<td><code>mock_obj.assert_called_with(10, key="value")</code></td>
</tr>
<tr>
<td><code>side_effect</code></td>
<td>Позволяет mock возвращать разные значения при каждом<br>вызове или выбрасывать исключения</td>
<td><code>mock_obj.side_effect = [1, 2, 3]</code></td>
</tr>
<tr>
<td><code>return_value</code></td>
<td>Значение, которое будет возвращено при вызове mock</td>
<td><code>mock_obj.return_value = 42</code></td>
</tr>
<tr>
<td><code>call_count</code></td>
<td>Количество вызовов mock</td>
<td><code>mock_obj.call_count == 2</code></td>
</tr>
<tr>
<td><code>patch.object()</code></td>
<td>Заменяет атрибут объекта (например, метод)</td>
<td><code>with patch.object(SomeClass, "method_name") as mock_method: ...</code></td>
</tr>
</tbody>
</table>
<h3>Пример использования <code>Mock</code></h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">unittest.mock</span> <span class="kn">import</span> <span class="n">Mock</span>

<span class="c1"># Создание mock-объекта</span>
<span class="n">mock_obj</span> <span class="o">=</span> <span class="n">Mock</span><span class="p">()</span>

<span class="c1"># Настройка возвращаемого значения</span>
<span class="n">mock_obj</span><span class="o">.</span><span class="n">some_method</span><span class="o">.</span><span class="n">return_value</span> <span class="o">=</span> <span class="s2">&quot;Mocked result&quot;</span>

<span class="c1"># Вызов mock-метода</span>
<span class="n">result</span> <span class="o">=</span> <span class="n">mock_obj</span><span class="o">.</span><span class="n">some_method</span><span class="p">()</span>

<span class="c1"># Проверка вызова</span>
<span class="n">mock_obj</span><span class="o">.</span><span class="n">some_method</span><span class="o">.</span><span class="n">assert_called_once</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">result</span><span class="p">)</span>  <span class="c1"># Выведет &quot;Mocked result&quot;</span>
</pre></div></div></div>

<h3>Пример использования <code>patch</code></h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">unittest</span> <span class="kn">import</span> <span class="n">TestCase</span>
<span class="kn">from</span> <span class="nn">unittest.mock</span> <span class="kn">import</span> <span class="n">patch</span>

<span class="k">class</span> <span class="nc">TestExternalDependency</span><span class="p">(</span><span class="n">TestCase</span><span class="p">):</span>
    <span class="nd">@patch</span><span class="p">(</span><span class="s2">&quot;module_with_dependency.external_function&quot;</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">test_external_function_mock</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">mock_external_function</span><span class="p">):</span>
        <span class="c1"># Настройка возвращаемого значения</span>
        <span class="n">mock_external_function</span><span class="o">.</span><span class="n">return_value</span> <span class="o">=</span> <span class="mi">10</span>

        <span class="c1"># Вызов функции, которая использует external_function</span>
        <span class="n">result</span> <span class="o">=</span> <span class="n">some_function</span><span class="p">()</span>

        <span class="c1"># Проверка вызова mock</span>
        <span class="n">mock_external_function</span><span class="o">.</span><span class="n">assert_called_once</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">assertEqual</span><span class="p">(</span><span class="n">result</span><span class="p">,</span> <span class="mi">10</span><span class="p">)</span>
</pre></div></div></div>

<h3><code>patch()</code> как декоратор</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="nd">@patch</span><span class="p">(</span><span class="s2">&quot;module_with_dependency.ClassName&quot;</span><span class="p">)</span>
<span class="k">def</span> <span class="nf">test_class_mock</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">MockClass</span><span class="p">):</span>
    <span class="n">mock_instance</span> <span class="o">=</span> <span class="n">MockClass</span><span class="o">.</span><span class="n">return_value</span>
    <span class="n">mock_instance</span><span class="o">.</span><span class="n">method</span><span class="o">.</span><span class="n">return_value</span> <span class="o">=</span> <span class="s2">&quot;Mocked&quot;</span>

    <span class="n">result</span> <span class="o">=</span> <span class="n">mock_instance</span><span class="o">.</span><span class="n">method</span><span class="p">()</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">assertEqual</span><span class="p">(</span><span class="n">result</span><span class="p">,</span> <span class="s2">&quot;Mocked&quot;</span><span class="p">)</span>
</pre></div></div></div>

<h3><code>side_effect</code> для имитации исключений или возвращаемых значений</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">unittest.mock</span> <span class="kn">import</span> <span class="n">Mock</span>

<span class="n">mock_func</span> <span class="o">=</span> <span class="n">Mock</span><span class="p">()</span>

<span class="c1"># Сценарий: возвращаем разные значения при каждом вызове</span>
<span class="n">mock_func</span><span class="o">.</span><span class="n">side_effect</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">]</span>

<span class="nb">print</span><span class="p">(</span><span class="n">mock_func</span><span class="p">())</span>  <span class="c1"># 1</span>
<span class="nb">print</span><span class="p">(</span><span class="n">mock_func</span><span class="p">())</span>  <span class="c1"># 2</span>
<span class="nb">print</span><span class="p">(</span><span class="n">mock_func</span><span class="p">())</span>  <span class="c1"># 3</span>

<span class="c1"># Сценарий: выброс исключения</span>
<span class="n">mock_func</span><span class="o">.</span><span class="n">side_effect</span> <span class="o">=</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">&quot;Some error&quot;</span><span class="p">)</span>
<span class="k">try</span><span class="p">:</span>
    <span class="n">mock_func</span><span class="p">()</span>
<span class="k">except</span> <span class="ne">ValueError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">e</span><span class="p">)</span>  <span class="c1"># &quot;Some error&quot;</span>
</pre></div></div></div>

<hr />
<h2>Дополнительные возможности <code>unittest</code></h2>
<h3>Запуск тестов с параметрами командной строки</h3>
<p>Вы можете использовать различные параметры при запуске <code>unittest</code> для изменения поведения тестов</p>
<ul>
<li><strong>Запуск тестов в verbose-режиме</strong> (подробный вывод)</li>
</ul>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span>python<span class="w"> </span>-m<span class="w"> </span>unittest<span class="w"> </span>-v<span class="w"> </span>test_module.py
</pre></div></div></div>

<ul>
<li><strong>Запуск тестов в quiet-режиме</strong> (минимальный вывод)</li>
</ul>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span>python<span class="w"> </span>-m<span class="w"> </span>unittest<span class="w"> </span>-q<span class="w"> </span>test_module.py
</pre></div></div></div>

<ul>
<li><strong>Остановка на первом неудачном тесте</strong></li>
</ul>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span>python<span class="w"> </span>-m<span class="w"> </span>unittest<span class="w"> </span>-f<span class="w"> </span>test_module.py
</pre></div></div></div>

<h3>Организация тестов с помощью Test Suites</h3>
<p>Test Suite позволяет группировать несколько тестов для более гибкой организации их выполнения</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">unittest</span>


<span class="c1"># Определение тестовых классов</span>
<span class="k">class</span> <span class="nc">TestClassA</span><span class="p">(</span><span class="n">unittest</span><span class="o">.</span><span class="n">TestCase</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">test_case_a</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">assertEqual</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span>

<span class="k">class</span> <span class="nc">TestClassB</span><span class="p">(</span><span class="n">unittest</span><span class="o">.</span><span class="n">TestCase</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">test_case_b</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">assertTrue</span><span class="p">(</span><span class="kc">True</span><span class="p">)</span>

<span class="c1"># Создание тестовой группы</span>
<span class="k">def</span> <span class="nf">suite</span><span class="p">():</span>
    <span class="n">suite</span> <span class="o">=</span> <span class="n">unittest</span><span class="o">.</span><span class="n">TestSuite</span><span class="p">()</span>
    <span class="n">suite</span><span class="o">.</span><span class="n">addTest</span><span class="p">(</span><span class="n">TestClassA</span><span class="p">(</span><span class="s1">&#39;test_case_a&#39;</span><span class="p">))</span>
    <span class="n">suite</span><span class="o">.</span><span class="n">addTest</span><span class="p">(</span><span class="n">TestClassB</span><span class="p">(</span><span class="s1">&#39;test_case_b&#39;</span><span class="p">))</span>
    <span class="k">return</span> <span class="n">suite</span>

<span class="c1"># Запуск тестов</span>
<span class="k">if</span> <span class="vm">__name__</span> <span class="o">==</span> <span class="s1">&#39;__main__&#39;</span><span class="p">:</span>
    <span class="n">runner</span> <span class="o">=</span> <span class="n">unittest</span><span class="o">.</span><span class="n">TextTestRunner</span><span class="p">()</span>
    <span class="n">runner</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="n">suite</span><span class="p">())</span>
</pre></div></div></div>

<h3>Тестирование исключений</h3>
<p>Вы можете проверять, выбрасывает ли код определенные исключения, с помощью <code>assertRaises</code></p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">unittest</span>

<span class="k">class</span> <span class="nc">TestExceptions</span><span class="p">(</span><span class="n">unittest</span><span class="o">.</span><span class="n">TestCase</span><span class="p">):</span>

    <span class="k">def</span> <span class="nf">test_exception</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">assertRaises</span><span class="p">(</span><span class="ne">ValueError</span><span class="p">):</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">&quot;Это исключение&quot;</span><span class="p">)</span>
</pre></div></div></div>

<h3>Тестирование с временем ожидания (таймаут)</h3>
<p>Для тестов, которые могут работать слишком долго, можно задать таймаут с помощью <code>timeout</code> параметра</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">unittest</span>


<span class="k">class</span> <span class="nc">TestTimeout</span><span class="p">(</span><span class="n">unittest</span><span class="o">.</span><span class="n">TestCase</span><span class="p">):</span>
    <span class="nd">@unittest</span><span class="o">.</span><span class="n">timeout</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>  <span class="c1"># 1 секунда</span>
    <span class="k">def</span> <span class="nf">test_timeout</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>  <span class="c1"># Этот тест завершится по таймауту</span>
            <span class="k">pass</span>
</pre></div></div></div>

<h3>Дополнительные библиотеки для тестирования</h3>
<ul>
<li><strong><code>pytest</code></strong> — альтернатива <code>unittest</code>, поддерживающая функции, не требующие классов для тестов, и имеющая мощные плагины.</li>
<li><strong><code>nose2</code></strong> — инструмент, который расширяет возможности <code>unittest</code> и имеет поддержку плагинов.</li>
<li><strong><code>hypothesis</code></strong> — библиотека для создания тестов на основе свойств (property-based testing), где тесты автоматически проверяют множество входных данных.</li>
</ul>
<hr />
<p>Эта расширенная шпаргалка включает не только базовую работу с <code>unittest</code>, но и подробное описание возможностей <code>unittest.mock</code> и других дополнительных возможностей для эффективного тестирования кода на Python.</p>