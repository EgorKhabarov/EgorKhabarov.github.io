<h1>XML - eXtensible Markup Language</h1>
<p>Расширяемый язык разметки, который используется для хранения и обмена структурированными данными.
Он использует теги для определения структуры данных и может быть использован для хранения
всех видов данных, включая текст, изображения и мультимедиа.
XML широко используется в Интернете для хранения и обмена данными между веб-сервисами и приложениями.
Пример</p>
<div class="code-element"><div class="lang-line"><text>xml</text><button class="copy-button" id="code779b" onclick="copyCode(code779, code779b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code779"><div class="highlight"><pre><span></span><span class="cp">&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;</span>
<span class="nt">&lt;note&gt;</span>
<span class="nt">&lt;to&gt;</span>Tove<span class="nt">&lt;/to&gt;</span>
<span class="nt">&lt;from&gt;</span>Jani<span class="nt">&lt;/from&gt;</span>
<span class="nt">&lt;heading&gt;</span>Reminder<span class="nt">&lt;/heading&gt;</span>
<span class="nt">&lt;body&gt;</span>Don&#39;t<span class="w"> </span>forget<span class="w"> </span>me<span class="w"> </span>this<span class="w"> </span>weekend!<span class="nt">&lt;/body&gt;</span>
<span class="nt">&lt;/note&gt;</span>
</pre></div></div></div>

<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code780b" onclick="copyCode(code780, code780b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code780"><div class="highlight"><pre><span></span><span class="c1"># config = ET.Element(&quot;config&quot;)</span>
<span class="c1"># bot = ET.SubElement(config, &quot;BOT&quot;)</span>
<span class="c1"># ET.SubElement(bot, &quot;bot_name&quot;).text = &quot;&quot;</span>
<span class="c1"># ET.SubElement(bot, &quot;token&quot;).text = &quot;&quot;</span>
<span class="c1"># tree = ET.ElementTree(config)</span>

<span class="kn">import</span> <span class="nn">xml.etree.ElementTree</span> <span class="k">as</span> <span class="nn">xml</span>

<span class="k">def</span> <span class="nf">dict_to_xml</span><span class="p">(</span><span class="n">dct</span><span class="p">,</span> <span class="n">root_node</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">root_node</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">root_node</span> <span class="o">=</span> <span class="n">xml</span><span class="o">.</span><span class="n">Element</span><span class="p">(</span><span class="s1">&#39;root&#39;</span><span class="p">)</span>
    <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">dct</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
        <span class="n">node</span> <span class="o">=</span> <span class="n">xml</span><span class="o">.</span><span class="n">SubElement</span><span class="p">(</span><span class="n">root_node</span><span class="p">,</span> <span class="n">key</span><span class="p">)</span>
        <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="nb">dict</span><span class="p">):</span>
            <span class="n">dict_to_xml</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">node</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">node</span><span class="o">.</span><span class="n">text</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">root_node</span>

<span class="k">def</span> <span class="nf">xml_to_dict</span><span class="p">(</span><span class="n">root</span><span class="p">):</span>
    <span class="kn">from</span> <span class="nn">collections</span> <span class="kn">import</span> <span class="n">defaultdict</span>
    <span class="n">dct</span> <span class="o">=</span> <span class="p">{</span><span class="n">root</span><span class="o">.</span><span class="n">tag</span><span class="p">:</span> <span class="p">{}</span> <span class="k">if</span> <span class="n">root</span><span class="o">.</span><span class="n">attrib</span> <span class="k">else</span> <span class="kc">None</span><span class="p">}</span>
    <span class="n">children</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">root</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">children</span><span class="p">:</span>
        <span class="n">dd</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">list</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">dc</span> <span class="ow">in</span> <span class="nb">map</span><span class="p">(</span><span class="n">xml_to_dict</span><span class="p">,</span> <span class="n">children</span><span class="p">):</span>
            <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">dc</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
                <span class="n">dd</span><span class="p">[</span><span class="n">k</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">v</span><span class="p">)</span>
        <span class="n">dct</span> <span class="o">=</span> <span class="p">{</span><span class="n">root</span><span class="o">.</span><span class="n">tag</span><span class="p">:</span> <span class="p">{</span><span class="n">k</span><span class="p">:</span> <span class="n">v</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">v</span><span class="p">)</span> <span class="o">==</span> <span class="mi">1</span> <span class="k">else</span> <span class="n">v</span> <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">dd</span><span class="o">.</span><span class="n">items</span><span class="p">()}}</span>
    <span class="k">if</span> <span class="n">root</span><span class="o">.</span><span class="n">attrib</span><span class="p">:</span>
        <span class="n">dct</span><span class="p">[</span><span class="n">root</span><span class="o">.</span><span class="n">tag</span><span class="p">]</span><span class="o">.</span><span class="n">update</span><span class="p">((</span><span class="s1">&#39;@&#39;</span> <span class="o">+</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span><span class="p">)</span> <span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">root</span><span class="o">.</span><span class="n">attrib</span><span class="o">.</span><span class="n">items</span><span class="p">())</span>
    <span class="k">if</span> <span class="n">root</span><span class="o">.</span><span class="n">text</span><span class="p">:</span>
        <span class="n">text</span> <span class="o">=</span> <span class="n">root</span><span class="o">.</span><span class="n">text</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
        <span class="k">if</span> <span class="n">children</span> <span class="ow">or</span> <span class="n">root</span><span class="o">.</span><span class="n">attrib</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">text</span><span class="p">:</span>
                <span class="n">dct</span><span class="p">[</span><span class="n">root</span><span class="o">.</span><span class="n">tag</span><span class="p">][</span><span class="s1">&#39;#text&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">text</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">dct</span><span class="p">[</span><span class="n">root</span><span class="o">.</span><span class="n">tag</span><span class="p">]</span> <span class="o">=</span> <span class="n">text</span>
    <span class="k">return</span> <span class="n">dct</span>

<span class="n">config</span> <span class="o">=</span> <span class="p">{</span><span class="s2">&quot;BOT&quot;</span><span class="p">:</span> <span class="p">{</span><span class="s2">&quot;bot_name&quot;</span><span class="p">:</span> <span class="s2">&quot;&quot;</span><span class="p">,</span> <span class="s2">&quot;token&quot;</span><span class="p">:</span> <span class="s2">&quot;&quot;</span><span class="p">}}</span>
<span class="n">config</span> <span class="o">=</span> <span class="n">dict_to_xml</span><span class="p">(</span><span class="n">config</span><span class="p">)</span>
<span class="n">tree</span> <span class="o">=</span> <span class="n">xml</span><span class="o">.</span><span class="n">ElementTree</span><span class="p">(</span><span class="n">config</span><span class="p">)</span>
<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">&quot;config.xml&quot;</span><span class="p">,</span> <span class="s1">&#39;wb&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
    <span class="n">tree</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">file</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s1">&#39;utf-8&#39;</span><span class="p">,</span> <span class="n">xml_declaration</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">&quot;config.xml&quot;</span><span class="p">,</span> <span class="s1">&#39;r&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
    <span class="n">tree</span> <span class="o">=</span> <span class="n">xml</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
<span class="n">root</span> <span class="o">=</span> <span class="n">tree</span><span class="o">.</span><span class="n">getroot</span><span class="p">()</span>
<span class="n">config</span> <span class="o">=</span> <span class="n">xml_to_dict</span><span class="p">(</span><span class="n">root</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">config</span><span class="p">)</span>
</pre></div></div></div>