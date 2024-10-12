<p><strong>Шаблонный движок</strong>: <code>Jinja3</code> — это шаблонный движок для <code>Python</code>,
который помогает отделить логику приложения от представления.
Это достигается за счет использования шаблонов для генерации HTML (или других текстовых форматов),
что позволяет легко изменять внешний вид и структуру выходных данных без изменения логики кода</p>
<p><strong>Переменные</strong>: В <code>Jinja3</code> переменные используются для динамической вставки данных в шаблон.
Они обозначаются двойными фигурными скобками <code>{{ variable }}</code>
и могут содержать любые данные, переданные из контекста рендеринга</p>
<h1>Basic usage</h1>
<div class="code_element"><div class="lang_line"><text>jinja</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-jinja"><div class="highlight"><pre><span></span><span class="x">- variable x has content: </span><span class="cp">{{</span> <span class="nv">x</span> <span class="cp">}}</span>
<span class="x">- expression: </span><span class="cp">{{</span> <span class="nv">x</span> <span class="o">+</span> <span class="m">1</span> <span class="cp">}}</span>
<span class="x">- escaped for HTML: </span><span class="cp">{{</span> <span class="nv">x</span> <span class="o">|</span> <span class="nf">e</span> <span class="cp">}}</span>
</pre></div></div></div>

<h1>Control structures</h1>
<div class="code_element"><div class="lang_line"><text>jinja</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-jinja"><div class="highlight"><pre><span></span><span class="cp">{%</span> <span class="k">for</span> <span class="nv">x</span> <span class="k">in</span> <span class="nv">range</span><span class="o">(</span><span class="m">5</span><span class="o">)</span> <span class="cp">%}</span>
<span class="x">    </span><span class="cp">{%</span> <span class="k">if</span> <span class="nv">x</span> <span class="o">%</span> <span class="m">2</span> <span class="o">==</span> <span class="m">0</span> <span class="cp">%}</span>
<span class="x">        </span><span class="cp">{{</span> <span class="nv">x</span> <span class="cp">}}</span><span class="x"> is even!</span>
<span class="x">    </span><span class="cp">{%</span> <span class="k">else</span> <span class="cp">%}</span>
<span class="x">        </span><span class="cp">{{</span> <span class="nv">x</span> <span class="cp">}}</span><span class="x"> is odd!</span>
<span class="x">    </span><span class="cp">{%</span> <span class="k">endif</span> <span class="cp">%}</span>
<span class="cp">{%</span> <span class="k">endfor</span> <span class="cp">%}</span>
</pre></div></div></div>

<h1>Whitespace trimming</h1>
<div class="code_element"><div class="lang_line"><text>jinja</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-jinja"><div class="highlight"><pre><span></span><span class="x">these are</span>
<span class="cp">{{</span> <span class="s2">&quot;three&quot;</span> <span class="cp">}}</span>
<span class="x">lines.</span>

<span class="x">this is conc</span>
<span class="cp">{{</span><span class="o">-</span> <span class="s2">&quot;at&quot;</span> -<span class="cp">}}</span>
<span class="x">enated.</span>
</pre></div></div></div>

<h1>Special blocks</h1>
<div class="code_element"><div class="lang_line"><text>jinja</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-jinja"><div class="highlight"><pre><span></span><span class="cp">{%</span> <span class="k">filter</span> <span class="nf">e</span> <span class="cp">%}</span>
<span class="cp">{%</span> <span class="k">raw</span> <span class="cp">%}</span>
    This is a raw block where {{nothing is evaluated}}
    {% not even this %}
    and &lt;html is escaped&gt; too with &quot;e&quot; filter
<span class="cp">{%</span> <span class="k">endraw</span> <span class="cp">%}</span>
<span class="cp">{%</span> <span class="k">endfilter</span> <span class="cp">%}</span>

<span class="cp">{%</span> <span class="k">macro</span> <span class="nv">myfunc</span><span class="o">(</span><span class="nv">x</span><span class="o">)</span> <span class="cp">%}</span>
<span class="x">    this is a reusable macro, with arguments: </span><span class="cp">{{</span><span class="nv">x</span><span class="cp">}}</span>
<span class="cp">{%</span> <span class="k">endmacro</span> <span class="cp">%}</span>

<span class="cp">{{</span> <span class="nv">myfunc</span><span class="o">(</span><span class="m">42</span><span class="o">)</span> <span class="cp">}}</span>

<span class="c">{#</span>
<span class="c">this is a comment</span>
<span class="c">#}</span>
</pre></div></div></div>

<h1>Inheritance</h1>
<div class="code_element"><div class="lang_line"><text>jinja</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button><button class="download_code_button" onclick="DownloadCode(this, `shared.html`)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 3v4a1 1 0 0 1-1 1H5m5 4-2 2 2 2m4-4 2 2-2 2m5-12v16a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V7.914a1 1 0 0 1 .293-.707l3.914-3.914A1 1 0 0 1 9.914 3H18a1 1 0 0 1 1 1Z"/></svg><text>Download code</text></button></div><div class="code language-jinja"><div class="highlight"><pre><span></span><span class="x">&lt;html&gt;</span>
<span class="x">  &lt;head&gt;</span>
<span class="x">    &lt;title&gt;</span><span class="cp">{%</span><span class="k">block</span> <span class="nv">title</span> <span class="cp">%}{%</span> <span class="k">endblock</span> <span class="cp">%}</span><span class="x">&lt;/title&gt;</span>
<span class="x">  &lt;/head&gt;</span>
<span class="x">  &lt;body&gt;</span>
<span class="x">    &lt;header&gt;&lt;h1&gt;</span><span class="cp">{%</span> <span class="k">block</span> <span class="nv">title</span> <span class="cp">%}{%</span> <span class="k">endblock</span> <span class="cp">%}</span><span class="x">&lt;/h1&gt;&lt;/header&gt;</span>
<span class="x">    &lt;main&gt;</span><span class="cp">{%</span> <span class="k">block</span> <span class="nv">content</span> <span class="cp">%}{%</span> <span class="k">endblock</span> <span class="cp">%}</span><span class="x">&lt;/main&gt;</span>
<span class="x">  &lt;/body&gt;</span>
<span class="x">&lt;/html&gt;</span>
</pre></div></div></div>

<div class="code_element"><div class="lang_line"><text>jinja</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button><button class="download_code_button" onclick="DownloadCode(this, `home.html`)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 3v4a1 1 0 0 1-1 1H5m5 4-2 2 2 2m4-4 2 2-2 2m5-12v16a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V7.914a1 1 0 0 1 .293-.707l3.914-3.914A1 1 0 0 1 9.914 3H18a1 1 0 0 1 1 1Z"/></svg><text>Download code</text></button></div><div class="code language-jinja"><div class="highlight"><pre><span></span><span class="cp">{%</span> <span class="k">extends</span> <span class="s2">&quot;shared.html&quot;</span> <span class="cp">%}</span>
<span class="cp">{%</span> <span class="k">block</span> <span class="nv">title</span> <span class="cp">%}</span><span class="x">Welcome to my site</span><span class="cp">{%</span> <span class="k">endblock</span> <span class="cp">%}</span>
<span class="cp">{%</span> <span class="k">block</span> <span class="nv">content</span> <span class="cp">%}</span>
<span class="x">This is the body</span>
<span class="cp">{%</span> <span class="k">endblock</span> <span class="cp">%}</span>
</pre></div></div></div>

<h1>Basic usage</h1>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">jinja2</span> <span class="kn">import</span> <span class="n">Template</span>
<span class="n">template</span> <span class="o">=</span> <span class="n">Template</span><span class="p">(</span><span class="s2">&quot;Hello {{ name }}!&quot;</span><span class="p">)</span>
<span class="n">template</span><span class="o">.</span><span class="n">render</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;John Doe&quot;</span><span class="p">)</span> <span class="o">==</span> <span class="sa">u</span><span class="s2">&quot;Hello John Doe!&quot;</span>
</pre></div></div></div>