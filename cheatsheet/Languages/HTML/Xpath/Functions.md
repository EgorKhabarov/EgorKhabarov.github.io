<h1>Node functions</h1>
<pre><code class="language-bash">name()                     # //[starts-with(name(), 'h')]
text()                     # //button[text()=&quot;Submit&quot;]
                           # //button/text()
lang(str)
namespace-uri()
</code></pre>
<pre><code class="language-bash">count()                    # //table[count(tr)=1]
position()                 # //ol/li[position()=2]
</code></pre>
<h1>Boolean functions</h1>
<pre><code class="language-bash">not(expr)                  # button[not(starts-with(text(),&quot;Submit&quot;))]
</code></pre>
<h1>String functions</h1>
<pre><code class="language-bash">contains()                 # font[contains(@class,&quot;head&quot;)]
starts-with()              # font[starts-with(@class,&quot;head&quot;)]
ends-with()                # font[ends-with(@class,&quot;head&quot;)]
</code></pre>
<pre><code class="language-bash">concat(x,y)
substring(str, start, len)
substring-before(&quot;01/02&quot;, &quot;/&quot;)  #=&gt; 01
substring-after(&quot;01/02&quot;, &quot;/&quot;)   #=&gt; 02
translate()
normalize-space()
string-length()
</code></pre>
<h1>Type conversion</h1>
<pre><code class="language-bash">string()
number()
boolean()
</code></pre>