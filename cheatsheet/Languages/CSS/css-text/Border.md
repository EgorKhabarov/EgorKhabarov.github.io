<h1 id="Border">Border</h1>
<div class="code-element">
    <div class="lang-line">
        <text>css</text>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="nt">border</span>
<span class="nt">border-width</span>
<span class="nt">border-style</span>
<span class="nt">border-color</span>

<span class="nt">border-width</span>
<span class="nt">thin</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">medium</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">thick</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">length</span>

<span class="nt">border-style</span>
<span class="nt">none</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">hidden</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">dotted</span>
<span class="nt">dashed</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">solid</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">double</span>
<span class="nt">groove</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">ridge</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">inset</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">outset</span>

<span class="nt">border-color</span>
<span class="nt">color</span>

<span class="nt">border-left</span>
<span class="nt">border-left-width</span>
<span class="nt">border-style</span>
<span class="nt">border-color</span>
<span class="nt">border-left-style</span>
<span class="nt">border-style</span>
<span class="nt">border-left-color</span>
<span class="nt">border-color</span>

<span class="nt">border-left-width</span>
<span class="nt">thin</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">medium</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">thick</span><span class="w"> </span><span class="nt">length</span>

<span class="nt">border-right</span>
<span class="nt">border-right-width</span>
<span class="nt">border-style</span>
<span class="nt">border-color</span>

<span class="nt">border-right-style</span>
<span class="nt">border-style</span>
<span class="nt">border-right-color</span>
<span class="nt">border-color</span>

<span class="nt">border-right-width</span>
<span class="nt">thin</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">medium</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">thick</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">length</span>

<span class="nt">border-top</span>
<span class="nt">border-top-width</span>
<span class="nt">border-style</span>
<span class="nt">border-color</span>
<span class="nt">border-top-style</span>
<span class="nt">border-style</span>







<span class="nt">border-top-color</span>
<span class="nt">border-color</span>

<span class="nt">border-top-width</span>
<span class="nt">thin</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">medium</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">thick</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">length</span>

<span class="nt">border-bottom</span>
<span class="nt">border-bottom-width</span>
<span class="nt">border-style</span>
<span class="nt">border-color</span>

<span class="nt">border-bottom-color</span>
<span class="nt">border-color</span>

<span class="nt">border-bottom-style</span>
<span class="nt">border-style</span>

<span class="nt">border-break</span>
<span class="nt">border-width</span>
<span class="nt">border-style</span>
<span class="nt">color</span>
<span class="nt">close</span>

<span class="nt">box-shadow</span>
<span class="nt">inset</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="o">[</span><span class="w"> </span><span class="nt">length</span><span class="o">,</span><span class="w"> </span><span class="nt">length</span><span class="o">,</span><span class="w"> </span><span class="nt">length</span><span class="o">,</span><span class="w"> </span><span class="nt">length</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="o">&lt;</span><span class="nt">color</span><span class="o">&gt;</span><span class="w"> </span><span class="o">]</span>
<span class="nt">none</span>

<span class="nt">border-collapse</span>
<span class="nt">collapse</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">separate</span>

<span class="nt">border-image</span>
<span class="nt">image</span>
<span class="o">[</span><span class="w"> </span><span class="nt">number</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="o">%</span><span class="w"> </span><span class="nt">border-width</span><span class="w"> </span><span class="nt">stretch</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">repeat</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="nt">round</span><span class="w"> </span><span class="o">]</span><span class="w"> </span><span class="nt">none</span>

<span class="nt">border-radius</span>
<span class="nt">border-radius</span>
<span class="nt">border-top-right-radius</span>
<span class="nt">border-bottom-right-radius</span>
<span class="nt">border-bottom-left-radius</span>
<span class="nt">border-top-left-radius</span>
<span class="nt">border-top-right-radius</span>
<span class="nt">length</span>
<span class="nt">border-bottom-left-radius</span>
<span class="nt">length</span>
<span class="nt">border-bottom-right-radius</span>
<span class="nt">length</span>
</pre></div></div>
</div>