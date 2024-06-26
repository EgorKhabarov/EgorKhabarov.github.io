<h1>Speech</h1>
<div class="code-element"><div class="lang-line"><text>css</text><button class="copy-button" id="code594b" onclick="copyCode(code594, code594b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code594"><div class="highlight"><pre><span></span><span class="nt">cue</span>
<span class="nt">cue-before</span>
<span class="nt">cue-after</span>

<span class="nt">cue</span><span class="w"> </span><span class="nt">before</span>
<span class="nt">url</span><span class="w"> </span><span class="o">[</span><span class="w"> </span><span class="nt">silent</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">x-soft</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">soft</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">medium</span>
<span class="nt">loud</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">x-loud</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">none</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">inherit</span><span class="w"> </span><span class="o">]</span>
<span class="nt">number</span>
<span class="o">%</span>

<span class="nt">cue-after</span>
<span class="nt">url</span><span class="w"> </span><span class="o">[</span><span class="w"> </span><span class="nt">silent</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">x-soft</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">soft</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">medium</span>
<span class="nt">loud</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">x-loud</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">none</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">inherit</span><span class="w"> </span><span class="o">]</span>
<span class="nt">number</span>
<span class="o">%</span>

<span class="nt">mark</span>
<span class="nt">mark-before</span>
<span class="nt">mark</span><span class="w"> </span><span class="nt">after</span>

<span class="nt">mark-before</span>
<span class="nt">string</span>

<span class="nt">mark-alter</span>
<span class="nt">string</span>

<span class="nt">voice-pitch-range</span>
<span class="nt">x-low</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">low</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">medium</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">high</span>
<span class="nt">xhigh</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">inherit</span>
<span class="nt">number</span>

<span class="nt">voice-stress</span>
<span class="nt">strong</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">moderate</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">none</span>
<span class="nt">reduced</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">inherit</span>

<span class="nt">voice-volume</span>
<span class="nt">silent</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">x</span><span class="w"> </span><span class="nt">soft</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">sofi</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">medium</span>
<span class="nt">loud</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">x-loud</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">inherit</span>
<span class="nt">number</span>
<span class="o">%</span>

<span class="nt">pause</span>
<span class="nt">pause-before</span>
<span class="nt">pause-after</span>

<span class="nt">pause-before</span>
<span class="nt">none</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">x-weak</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">weak</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">medium</span>
<span class="nt">strong</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">x-strong</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">inherit</span>
<span class="nt">time</span>

<span class="nt">pause</span><span class="w"> </span><span class="nt">after</span>
<span class="nt">none</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">x-weak</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">weak</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">medium</span>
<span class="nt">strong</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">x-strong</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">inherit</span>
<span class="nt">time</span>

<span class="nt">phonemes</span>
<span class="nt">string</span>

<span class="nt">voice-duration</span>
<span class="nt">time</span>

<span class="nt">voice-family</span>
<span class="nt">inherit</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="o">[</span><span class="w"> </span><span class="o">&lt;</span><span class="nt">specific-voice</span><span class="o">,</span><span class="w"> </span><span class="nt">age</span><span class="o">,</span>
<span class="nt">generic-voice</span><span class="o">,</span><span class="w"> </span><span class="nt">number</span><span class="o">&gt;</span><span class="w"> </span><span class="o">]</span>

<span class="nt">voice-rate</span>
<span class="nt">x-slow</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">slow</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">medium</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">fast</span>
<span class="nt">x-fast</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">inherit</span>

<span class="nt">voice-pitch</span>
<span class="nt">x-low</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">low</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">medium</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">high</span>
<span class="nt">x-high</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">inherit</span>
<span class="nt">number</span>
<span class="o">%</span>

<span class="nt">caption-side</span>
<span class="nt">top</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">bottom</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">left</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">right</span>

<span class="nt">rest</span>
<span class="nt">rest-before</span>
<span class="nt">rest-alter</span>

<span class="nt">rest-before</span>
<span class="nt">none</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">x-weak</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">weak</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">medium</span>
<span class="nt">strong</span>
<span class="o">|</span><span class="w"> </span><span class="nt">x-strong</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">inherit</span>
<span class="nt">time</span>

<span class="nt">rest</span><span class="w"> </span><span class="nt">after</span>
<span class="nt">none</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">x-weak</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">weak</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">medium</span>
<span class="nt">x-strong</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">inherit</span>

<span class="nt">speak</span>
<span class="nt">none</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">normal</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">spell-out</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">digits</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">literal-punctuation</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">no-punctuation</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">inherit-number</span>
</pre></div></div></div>