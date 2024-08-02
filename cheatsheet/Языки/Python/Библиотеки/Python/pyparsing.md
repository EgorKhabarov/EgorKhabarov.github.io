<p>Библиотека "pyparsing" используется для анализа и разбора текстовых данных в языке программирования Python.
Она предоставляет возможность создавать грамматики и правила для разбора сложных структур данных.</p>
<p>Методы модуля "pyparsing" и его подмодулей:</p>
<p>parseString(string) - Разбирает строку в соответствии с определенной грамматикой и возвращает структурированные данные.
Word(alphas) - Определяет грамматическое правило для разбора последовательности символов, состоящей только из букв.
nums - Подмодуль, содержащий грамматические правила для разбора числовых значений.
CaselessLiteral(string) - Определяет грамматическое правило для разбора нечувствительных к регистру строк.
QuotedString(quoteChar) - Определяет грамматическое правило для разбора строки, заключенной в кавычки.</p>
<p>Самые часто используемые методы "pyparsing" с их кратким описанием и примером кода:</p>
<p>parseString(string): Разбирает строку в соответствии с грамматикой и возвращает структурированные данные.</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="code22c8863e87b512e299c017cc8cf697e0b"
          onclick="copyCode(code22c8863e87b512e299c017cc8cf697e0, code22c8863e87b512e299c017cc8cf697e0b)">
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
<div class="code" id="code22c8863e87b512e299c017cc8cf697e0"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">pyparsing</span> <span class="kn">import</span> <span class="n">Word</span><span class="p">,</span> <span class="n">alphas</span><span class="p">,</span> <span class="n">nums</span>

<span class="n">data</span> <span class="o">=</span> <span class="s2">&quot;Hello World&quot;</span>
<span class="nb">print</span><span class="p">(</span><span class="n">Word</span><span class="p">(</span><span class="n">alphas</span><span class="p">)</span><span class="o">.</span><span class="n">parseString</span><span class="p">(</span><span class="n">data</span><span class="p">))</span>  <span class="c1"># [&quot;Hello&quot;]</span>
</pre></div></div>
</div>

<p>Word(alphas): Определяет грамматическое правило для разбора последовательности символов, состоящей только из букв.</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="codebfb7d6ee52845a3f95d551377a239b9ab"
          onclick="copyCode(codebfb7d6ee52845a3f95d551377a239b9a, codebfb7d6ee52845a3f95d551377a239b9ab)">
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
<div class="code" id="codebfb7d6ee52845a3f95d551377a239b9a"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">pyparsing</span> <span class="kn">import</span> <span class="n">Word</span><span class="p">,</span> <span class="n">alphas</span>

<span class="n">data</span> <span class="o">=</span> <span class="s2">&quot;Hello123&quot;</span>
<span class="nb">print</span><span class="p">(</span><span class="n">Word</span><span class="p">(</span><span class="n">alphas</span><span class="p">)</span><span class="o">.</span><span class="n">parseString</span><span class="p">(</span><span class="n">data</span><span class="p">))</span>  <span class="c1"># [&quot;Hello&quot;]</span>
</pre></div></div>
</div>

<p>QuotedString(quoteChar): Определяет грамматическое правило для разбора строки, заключенной в кавычки.</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="codece663a7f2130189c00a0b9a207442cd3b"
          onclick="copyCode(codece663a7f2130189c00a0b9a207442cd3, codece663a7f2130189c00a0b9a207442cd3b)">
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
<div class="code" id="codece663a7f2130189c00a0b9a207442cd3"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">pyparsing</span> <span class="kn">import</span> <span class="n">QuotedString</span>

<span class="n">data</span> <span class="o">=</span> <span class="s1">&#39;&quot;Hello World&quot;&#39;</span>
<span class="nb">print</span><span class="p">(</span><span class="n">QuotedString</span><span class="p">(</span><span class="s1">&#39;&quot;&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">parseString</span><span class="p">(</span><span class="n">data</span><span class="p">))</span>  <span class="c1"># [&quot;Hello World&quot;]</span>
</pre></div></div>
</div>