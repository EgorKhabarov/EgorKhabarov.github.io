<pre><code class="language-python">def sqrt(x, p: int = 2):
    return pow(x, (1 / p))
</code></pre>
<pre><code class="language-python">def rgb_to_hex(r: int, g: int, b: int) -&gt; str:
    return &quot;#{:02x}{:02x}{:02x}&quot;.format(r, g, b).upper()

def hex_to_rgb(h: str) -&gt; tuple[int, int, int]:
    return tuple(int(h.lstrip(&quot;#&quot;)[i:i + 2], 16) for i in (0, 2, 4))
</code></pre>
<pre><code class="language-pycon">&gt;&gt;&gt; rgb_to_hex(164, 73, 211)
&quot;#A449D3&quot;
&gt;&gt;&gt; hex_to_rgb(&quot;#A449D3&quot;)
(164, 73, 211)
</code></pre>
<pre><code class="language-python">def html_escape(text):
    return &quot;&quot;.join(f&quot;&amp;#{ord(char)};&quot; for char in text)
</code></pre>
<pre><code class="language-python">def tg_color(chat_id: int):
    &quot;&quot;&quot;
    0x6FB9F0 Синий
    0xFFD67E Оранжевый
    0xCB86DB Фиолетовый
    0x8EEE98 Зелёный
    0xFF93B2 Розовый
    0xFB6F5F Красный
    &quot;&quot;&quot;
    return {0: &quot;К&quot;, 1: &quot;О&quot;, 2: &quot;Ф&quot;, 3: &quot;З&quot;, 4: &quot;Г&quot;, 5: &quot;С&quot;, 6: &quot;Р&quot;}[abs(chat_id) % 7]
</code></pre>
<pre><code class="language-python">def unicode(text):
    return &quot;&quot;.join(fr&quot;\U{ord(char):0&gt;8x}&quot; for char in text)
</code></pre>