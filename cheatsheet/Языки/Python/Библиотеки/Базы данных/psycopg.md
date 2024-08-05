<div class="code-element">
<div class="lang-line">
  <text>bash</text>
  <button class="copy-button"
          id="code1c2b830ee1431f384aff2e6ad3ec11e7b"
          onclick="copyCode(code1c2b830ee1431f384aff2e6ad3ec11e7, code1c2b830ee1431f384aff2e6ad3ec11e7b)">
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
<div class="code" id="code1c2b830ee1431f384aff2e6ad3ec11e7"><div class="highlight"><pre><span></span>pip<span class="w"> </span>install<span class="w"> </span>-U<span class="w"> </span>psycopg
</pre></div></div>
</div>
<div class="code-element">
<div class="lang-line">
  <text>bash</text>
  <button class="copy-button"
          id="code3a3538def17a3b9c467af6bff0289463b"
          onclick="copyCode(code3a3538def17a3b9c467af6bff0289463, code3a3538def17a3b9c467af6bff0289463b)">
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
<div class="code" id="code3a3538def17a3b9c467af6bff0289463"><div class="highlight"><pre><span></span>pip<span class="w"> </span>install<span class="w"> </span>-U<span class="w"> </span>psycopg2
</pre></div></div>
</div>

<p>Базовые команды SQL
Создать/изменить/удалить объект СУБД
CREATE | ALTER | DROP</p>
<p>Вставить/изменить/удалить записи [таблицы]
INSERT | UPDATE | DELETE/TRUNCATE</p>
<p>Получить выборку записей
SELECT</p>
<div class="code-element">
<div class="lang-line">
  <text>sql</text>
  <button class="copy-button"
          id="code981f9e641f61d011334018d54ab6f416b"
          onclick="copyCode(code981f9e641f61d011334018d54ab6f416, code981f9e641f61d011334018d54ab6f416b)">
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
<div class="code" id="code981f9e641f61d011334018d54ab6f416"><div class="highlight"><pre><span></span><span class="k">CREATE</span><span class="w"> </span><span class="k">ACCESS</span><span class="w"> </span><span class="k">METHOD</span>
<span class="k">CREATE</span><span class="w"> </span><span class="k">AGGREGATE</span>
<span class="k">CREATE</span><span class="w"> </span><span class="k">CAST</span>
<span class="k">CREATE</span><span class="w"> </span><span class="k">COLLATION</span>
<span class="k">CREATE</span><span class="w"> </span><span class="k">CONVERSION</span>
<span class="k">CREATE</span><span class="w"> </span><span class="k">DATABASE</span><span class="w"> </span><span class="c1">-- Создание базы данных</span>
<span class="k">CREATE</span><span class="w"> </span><span class="k">DOMAIN</span>
<span class="k">CREATE</span><span class="w"> </span><span class="n">EVENT</span><span class="w"> </span><span class="k">TRIGGER</span>
<span class="k">CREATE</span><span class="w"> </span><span class="n">EXTENSION</span>
<span class="k">CREATE</span><span class="w"> </span><span class="k">FOREIGN</span><span class="w"> </span><span class="k">DATA</span><span class="w"> </span><span class="n">WRAPPER</span>
<span class="k">CREATE</span><span class="w"> </span><span class="k">FOREIGN</span><span class="w"> </span><span class="k">TABLE</span>
<span class="k">CREATE</span><span class="w"> </span><span class="k">FUNCTION</span>
<span class="k">CREATE</span><span class="w"> </span><span class="k">GROUP</span>
<span class="k">CREATE</span><span class="w"> </span><span class="k">INDEX</span>
<span class="k">CREATE</span><span class="w"> </span><span class="k">LANGUAGE</span>
<span class="k">CREATE</span><span class="w"> </span><span class="n">MATERIALIZED</span><span class="w"> </span><span class="k">VIEW</span>
<span class="k">CREATE</span><span class="w"> </span><span class="k">OPERATOR</span>
<span class="k">CREATE</span><span class="w"> </span><span class="k">OPERATOR</span><span class="w"> </span><span class="k">CLASS</span>
<span class="k">CREATE</span><span class="w"> </span><span class="k">OPERATOR</span><span class="w"> </span><span class="n">FAMILY</span>
<span class="k">CREATE</span><span class="w"> </span><span class="n">POLICY</span>
<span class="k">CREATE</span><span class="w"> </span><span class="k">PROCEDURE</span>
<span class="k">CREATE</span><span class="w"> </span><span class="n">PUBLICATION</span>
<span class="k">CREATE</span><span class="w"> </span><span class="k">ROLE</span><span class="w"> </span><span class="c1">-- Роли базы данных</span>
<span class="k">CREATE</span><span class="w"> </span><span class="k">RULE</span>
<span class="k">CREATE</span><span class="w"> </span><span class="k">SCHEMA</span>
<span class="k">CREATE</span><span class="w"> </span><span class="n">SEQUENCE</span>
<span class="k">CREATE</span><span class="w"> </span><span class="n">SERVER</span>
<span class="k">CREATE</span><span class="w"> </span><span class="k">STATISTICS</span>
<span class="k">CREATE</span><span class="w"> </span><span class="n">SUBSCRIPTION</span>
<span class="k">CREATE</span><span class="w"> </span><span class="k">TABLE</span><span class="w"> </span><span class="c1">-- Создание таблицы</span>
<span class="k">CREATE</span><span class="w"> </span><span class="k">TABLE</span><span class="w"> </span><span class="k">AS</span>
<span class="k">CREATE</span><span class="w"> </span><span class="n">TABLESPACE</span><span class="w"> </span><span class="c1">-- Табличные пространства</span>
<span class="k">CREATE</span><span class="w"> </span><span class="nb">TEXT</span><span class="w"> </span><span class="k">SEARCH</span><span class="w"> </span><span class="n">CONFIGURATION</span>
<span class="k">CREATE</span><span class="w"> </span><span class="nb">TEXT</span><span class="w"> </span><span class="k">SEARCH</span><span class="w"> </span><span class="k">DICTIONARY</span>
<span class="k">CREATE</span><span class="w"> </span><span class="nb">TEXT</span><span class="w"> </span><span class="k">SEARCH</span><span class="w"> </span><span class="n">PARSER</span>
<span class="k">CREATE</span><span class="w"> </span><span class="nb">TEXT</span><span class="w"> </span><span class="k">SEARCH</span><span class="w"> </span><span class="k">TEMPLATE</span>
<span class="k">CREATE</span><span class="w"> </span><span class="k">TRANSFORM</span>
<span class="k">CREATE</span><span class="w"> </span><span class="k">TRIGGER</span>
<span class="k">CREATE</span><span class="w"> </span><span class="k">TYPE</span>
<span class="k">CREATE</span><span class="w"> </span><span class="k">USER</span>
<span class="k">CREATE</span><span class="w"> </span><span class="k">USER</span><span class="w"> </span><span class="n">MAPPING</span>
<span class="k">CREATE</span><span class="w"> </span><span class="k">VIEW</span>
</pre></div></div>
</div>

<div class="code-element">
<div class="lang-line">
  <text>sql</text>
  <button class="copy-button"
          id="code8216c062f95f99617376ed47ca660c67b"
          onclick="copyCode(code8216c062f95f99617376ed47ca660c67, code8216c062f95f99617376ed47ca660c67b)">
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
<div class="code" id="code8216c062f95f99617376ed47ca660c67"><div class="highlight"><pre><span></span><span class="k">CREATE</span><span class="w"> </span><span class="k">DATABASE</span><span class="w"> </span><span class="n">tst</span><span class="p">;</span>

<span class="k">CREATE</span><span class="w"> </span><span class="k">TABLE</span><span class="w"> </span><span class="n">tbl</span><span class="p">(</span>
<span class="w">    </span><span class="n">k</span><span class="w"> </span><span class="nb">integer</span><span class="p">,</span><span class="w">  </span><span class="c1">-- Имя поля Тип поля</span>
<span class="w">    </span><span class="n">v</span><span class="w"> </span><span class="nb">text</span>
<span class="p">);</span>
</pre></div></div>
</div>

<div class="code-element">
<div class="lang-line">
  <text>sql</text>
  <button class="copy-button"
          id="code6b7a69471d0308ccd8d94dd8775e3126b"
          onclick="copyCode(code6b7a69471d0308ccd8d94dd8775e3126, code6b7a69471d0308ccd8d94dd8775e3126b)">
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
<div class="code" id="code6b7a69471d0308ccd8d94dd8775e3126"><div class="highlight"><pre><span></span><span class="c1">-- это однострочный комментарий</span>
<span class="cm">/* а это -</span>
<span class="cm">         - многострочный */</span>

<span class="n">fld</span><span class="w">      </span><span class="c1">-- это поле/столбец</span>
<span class="n">Fld</span><span class="w">      </span><span class="c1">-- это то же самое поле</span>
<span class="n">FLD</span><span class="w">      </span><span class="c1">-- ... и это – все оно же (приводится к lower case)</span>

<span class="ss">&quot;Fld&quot;</span><span class="w">    </span><span class="c1">-- а вот это – тоже поле, но совсем другое (кавычки дают регистрозависимость)</span>

<span class="s1">&#39;str&#39;</span><span class="w">    </span><span class="c1">-- это строка</span>

<span class="s1">&#39;st&#39;&#39;r&#39;</span><span class="w">  </span><span class="c1">-- это строка с одинарным апострофом</span>
<span class="n">E</span><span class="s1">&#39;st\&#39;</span><span class="n">r</span><span class="s1">&#39; -- ... и это – она же</span>
<span class="s1">$$st&#39;</span><span class="n">r$$</span><span class="w"> </span><span class="c1">-- ... и даже вот это</span>
<span class="err">$</span><span class="n">abcd$st</span><span class="err">&#39;</span><span class="n">r$abcd$</span>
</pre></div></div>
</div>

<p><strong>Все поля регистронезависимы</strong> – как бы и где бы вы его не написали, оно будет приведено к нижнему регистру.
Если же вам хочется указать для поля «странное» имя – например, с пробелом, по-русски, по-китайски,
или просто сохранить его регистр, то указывать его надо везде в обычных двойных кавычках
никаких странностей вроде квадратных скобок или обратных апострофов.</p>