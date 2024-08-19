<h1>Node functions</h1>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span>name<span class="o">()</span><span class="w">                     </span><span class="c1"># //[starts-with(name(), &#39;h&#39;)]</span>
text<span class="o">()</span><span class="w">                     </span><span class="c1"># //button[text()=&quot;Submit&quot;]</span>
<span class="w">                           </span><span class="c1"># //button/text()</span>
lang<span class="o">(</span>str<span class="o">)</span>
namespace-uri<span class="o">()</span>
</pre></div></div></div>

<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span>count<span class="o">()</span><span class="w">                    </span><span class="c1"># //table[count(tr)=1]</span>
position<span class="o">()</span><span class="w">                 </span><span class="c1"># //ol/li[position()=2]</span>
</pre></div></div></div>

<h1>Boolean functions</h1>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span>not<span class="o">(</span>expr<span class="o">)</span><span class="w">                  </span><span class="c1"># button[not(starts-with(text(),&quot;Submit&quot;))]</span>
</pre></div></div></div>

<h1>String functions</h1>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span>contains<span class="o">()</span><span class="w">                 </span><span class="c1"># font[contains(@class,&quot;head&quot;)]</span>
starts-with<span class="o">()</span><span class="w">              </span><span class="c1"># font[starts-with(@class,&quot;head&quot;)]</span>
ends-with<span class="o">()</span><span class="w">                </span><span class="c1"># font[ends-with(@class,&quot;head&quot;)]</span>
</pre></div></div></div>

<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span>concat<span class="o">(</span>x,y<span class="o">)</span>
substring<span class="o">(</span>str,<span class="w"> </span>start,<span class="w"> </span>len<span class="o">)</span>
substring-before<span class="o">(</span><span class="s2">&quot;01/02&quot;</span>,<span class="w"> </span><span class="s2">&quot;/&quot;</span><span class="o">)</span><span class="w">  </span><span class="c1">#=&gt; 01</span>
substring-after<span class="o">(</span><span class="s2">&quot;01/02&quot;</span>,<span class="w"> </span><span class="s2">&quot;/&quot;</span><span class="o">)</span><span class="w">   </span><span class="c1">#=&gt; 02</span>
translate<span class="o">()</span>
normalize-space<span class="o">()</span>
string-length<span class="o">()</span>
</pre></div></div></div>

<h1>Type conversion</h1>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span>string<span class="o">()</span>
number<span class="o">()</span>
boolean<span class="o">()</span>
</pre></div></div></div>