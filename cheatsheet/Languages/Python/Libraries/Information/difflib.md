<h4>SequenceMatcher</h4>
<p>Сравнение двух последовательностей и определение степени их сходства.</p>
<pre><code class="language-python">import difflib

s1 = &quot;Hello, world!&quot;
s2 = &quot;Hello, everyone!&quot;

matcher = difflib.SequenceMatcher(None, s1, s2)
ratio = matcher.ratio()

print(f&quot;Similarity ratio: {ratio}&quot;)

&quot;&quot;&quot;Similarity ratio: 0.6206896551724138&quot;&quot;&quot;
</code></pre>
<h4>get_close_matches</h4>
<p>Нахождение наиболее похожей строки в наборе строк на основе заданной строки.</p>
<pre><code class="language-python">import difflib

colors = [&quot;red&quot;, &quot;green&quot;, &quot;blue&quot;, &quot;yellow&quot;]
color = &quot;grea&quot;

matches = difflib.get_close_matches(color, colors)

print(f&quot;Closest matches: {matches}&quot;)

&quot;&quot;&quot;Closest matches: [&quot;green&quot;]&quot;&quot;&quot;
</code></pre>
<h4>unified_diff</h4>
<p>Генерация отчета о различиях между двумя последовательностями.</p>
<pre><code class="language-python">import difflib

text1 = &quot;&quot;&quot;Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.&quot;&quot;&quot;

text2 = &quot;&quot;&quot;Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua.&quot;&quot;&quot;

d = difflib.unified_diff(text1.splitlines(), text2.splitlines())

print(&quot;\n&quot;.join(d))

&quot;&quot;&quot;
---

+++

@@ -1,3 +1,3 @@

 Lorem ipsum dolor sit amet,
 consectetur adipiscing elit,
-sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
+sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua.
&quot;&quot;&quot;
</code></pre>
<h4>HtmlDiff</h4>
<p>Генерация отчета о различиях между двумя последовательностями в формате HTML.</p>
<pre><code class="language-python">import difflib

text1 = &quot;&quot;&quot;Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.&quot;&quot;&quot;

text2 = &quot;&quot;&quot;Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua.&quot;&quot;&quot;

d = difflib.HtmlDiff().make_file(text1.splitlines(), text2.splitlines())

with open(&quot;diff.html&quot;, &quot;w&quot;) as f:
    f.writelines(d)
</code></pre>
<h4>context_diff</h4>
<p>Генерация отчета о различиях между двумя последовательностями в формате context diff.</p>
<pre><code class="language-python">import difflib

text1 = &quot;&quot;&quot;Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.&quot;&quot;&quot;

text2 = &quot;&quot;&quot;Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua.&quot;&quot;&quot;

d = difflib.context_diff(text1.splitlines(), text2.splitlines())

print(&quot;\n&quot;.join(d))

&quot;&quot;&quot;
***

---

***************

*** 1,3 ****

  Lorem ipsum dolor sit amet,
  consectetur adipiscing elit,
! sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
--- 1,3 ----

  Lorem ipsum dolor sit amet,
  consectetur adipiscing elit,
! sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua.
&quot;&quot;&quot;
</code></pre>
<h4>ndiff</h4>
<p>Генерация отчета о различиях между двумя последовательностями в формате ndiff.</p>
<pre><code class="language-python">import difflib

text1 = &quot;&quot;&quot;Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.&quot;&quot;&quot;

text2 = &quot;&quot;&quot;Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua.&quot;&quot;&quot;

d = difflib.ndiff(text1.splitlines(), text2.splitlines())

print(&quot;\n&quot;.join(d))

&quot;&quot;&quot;
  Lorem ipsum dolor sit amet,
  consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
?                                                          ^

+ sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua.
?                                                          ^^       
&quot;&quot;&quot;
</code></pre>
<h4>isjunk и ignore</h4>
<p>Использование пользовательских функций для игнорирования символов при сравнении последовательностей.</p>
<pre><code class="language-python">import difflib

def isjunk(s):
    return s in [&quot; &quot;, &quot;\n&quot;]

text1 = &quot;&quot;&quot;Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.&quot;&quot;&quot;

text2 = &quot;&quot;&quot;Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua.&quot;&quot;&quot;

matcher = difflib.SequenceMatcher(isjunk, text1, text2)
ratio = matcher.ratio()

print(f&quot;Similarity ratio: {ratio}&quot;)

&quot;&quot;&quot;Similarity ratio: 0.9878542510121457&quot;&quot;&quot;
</code></pre>
<h4>reduce_func</h4>
<p>Использование пользовательской функции для преобразования различий в отчете о сравнении.</p>
<pre><code class="language-python">import difflib

text1 = &quot;&quot;&quot;Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.&quot;&quot;&quot;

text2 = &quot;&quot;&quot;Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua.&quot;&quot;&quot;

d = difflib.Differ()
diff = d.compare(text1.splitlines(), text2.splitlines())

def reduce_func(s):
    if s.startswith(&quot;- &quot;):
        return f&quot;&lt;span style=&quot;color:red&quot;&gt;{s}&lt;/span&gt;&quot;
    elif s.startswith(&quot;+ &quot;):
        return f&quot;&lt;span style=&quot;color:green&quot;&gt;{s}&lt;/span&gt;&quot;
    else:
        return s

diff = map(reduce_func, diff)
diff = &quot;\n&quot;.join(diff)

print(diff)

&quot;&quot;&quot;
  Lorem ipsum dolor sit amet,
  consectetur adipiscing elit,
&lt;span style=&quot;color:red&quot;&gt;- sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.&lt;/span&gt;
?                                                          ^

&lt;span style=&quot;color:green&quot;&gt;+ sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua.&lt;/span&gt;
?                                                          ^^                                         
&quot;&quot;&quot;
</code></pre>