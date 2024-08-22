<h1>Box Model</h1>
<div class="code_element"><div class="lang_line"><text>css</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-css"><div class="highlight"><pre><span></span><span class="nt">float</span>
<span class="nt">left</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">right</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">none</span>

<span class="nt">height</span>
<span class="nt">auto</span>
<span class="nt">length</span>
<span class="o">%</span>

<span class="nt">max-height</span>
<span class="nt">none</span>
<span class="nt">length</span>
<span class="o">%</span>

<span class="nt">max-width</span>
<span class="nt">none</span>
<span class="nt">length</span>
<span class="o">%</span>

<span class="nt">min-height</span>
<span class="nt">none</span>
<span class="nt">length</span>
<span class="o">%</span>

<span class="nt">width</span>
<span class="nt">auto</span>
<span class="o">%</span>
<span class="nt">length</span>

<span class="nt">margin-top</span>
<span class="nt">margin-right</span>
<span class="nt">margin-bottom</span>
<span class="nt">margin-left</span>

<span class="nt">margin-bottom</span>
<span class="nt">auto</span>
<span class="nt">length</span>
<span class="o">%</span>

<span class="nt">margin-left</span>
<span class="nt">auto</span>
<span class="nt">height</span>
<span class="o">%</span>

<span class="nt">margin-right</span>
<span class="nt">auto</span>
<span class="nt">height</span>
<span class="o">%</span>

<span class="nt">margin-top</span>
<span class="nt">auto</span>
<span class="nt">length</span>
<span class="nt">max-width</span>





<span class="nt">padding</span>
<span class="nt">padding-top</span>
<span class="nt">padding-right</span>
<span class="nt">padding-bottom</span>
<span class="nt">padding-left</span>

<span class="nt">podding-bottom</span>
<span class="nt">length</span>
<span class="o">%</span>

<span class="nt">padding-left</span>
<span class="nt">length</span>
<span class="o">%</span>

<span class="nt">padding-right</span>
<span class="nt">length</span>
<span class="o">%</span>

<span class="nt">padding-top</span>
<span class="nt">length</span>
<span class="o">%</span>

<span class="nt">display</span>
<span class="nt">none</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">inline</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">block</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">inline-block</span>
<span class="nt">list-item</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">run-in</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">compact</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">table</span>
<span class="nt">inline-table</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">table-row-group</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">table-header-group</span>
<span class="nt">table-footer-group</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">table-row</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">table-column-group</span>
<span class="nt">table-column</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">table-cell</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">table-caption</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">ruby</span>
<span class="nt">ruby-base</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">ruby-text</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">ruby-base-group</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">ruby-text-group</span>
<span class="nt">inline-flex</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">inline-grid</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">contents</span>

<span class="nt">overflow</span>
<span class="nt">visible</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">hidden</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">scroll</span>
<span class="nt">auto</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">no-display</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">no-content</span>
<span class="nt">overflow-x</span>
<span class="nt">overflow-y</span>

<span class="nt">overflow-style</span>
<span class="nt">auto</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">marquee-line</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">marqueeblock</span>

<span class="nt">overflow-x</span>
<span class="nt">visible</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">hidden</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">scroll</span>
<span class="nt">auto</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">no-display</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">no-content</span>

<span class="nt">rotation</span>
<span class="nt">angle</span>

<span class="nt">rotation-point</span>
<span class="nt">position</span><span class="w"> </span><span class="o">(</span><span class="nt">paired</span><span class="w"> </span><span class="nt">value</span><span class="w"> </span><span class="nt">off-set</span><span class="o">)</span>

<span class="nt">visibility</span>
<span class="nt">visible</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">hidden</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">collapse</span>
<span class="nt">clear</span>
<span class="nt">left</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">right</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">both</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">none</span>
</pre></div></div></div>