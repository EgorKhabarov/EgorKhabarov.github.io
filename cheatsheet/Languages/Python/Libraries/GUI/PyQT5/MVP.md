<p>minimum viable product</p>
<p><a href="https://itproger.com/course/python-pyqt5/2">https://itproger.com/course/python-pyqt5/2</a></p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>

<span class="kn">from</span> <span class="nn">PyQt5</span> <span class="kn">import</span> <span class="n">QtWidgets</span>
<span class="kn">from</span> <span class="nn">PyQt5.QtWidgets</span> <span class="kn">import</span> <span class="n">QApplication</span><span class="p">,</span> <span class="n">QMainWindow</span>


<span class="k">def</span> <span class="nf">application</span><span class="p">():</span>
    <span class="n">app</span> <span class="o">=</span> <span class="n">QApplication</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">)</span>
    <span class="n">window</span> <span class="o">=</span> <span class="n">QMainWindow</span><span class="p">()</span>

    <span class="n">window</span><span class="o">.</span><span class="n">setWindowTitle</span><span class="p">(</span><span class="s2">&quot;WindowTitle&quot;</span><span class="p">)</span>
    <span class="n">window</span><span class="o">.</span><span class="n">setGeometry</span><span class="p">(</span><span class="mi">300</span><span class="p">,</span> <span class="mi">250</span><span class="p">,</span> <span class="mi">500</span><span class="p">,</span> <span class="mi">300</span><span class="p">)</span>

    <span class="n">window</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
    <span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="n">app</span><span class="o">.</span><span class="n">exec_</span><span class="p">())</span>


<span class="k">if</span> <span class="vm">__name__</span> <span class="o">==</span> <span class="s2">&quot;__main__&quot;</span><span class="p">:</span>
    <span class="n">application</span><span class="p">()</span>
</pre></div></div></div>