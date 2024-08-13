<h2>Me:</h2>
<p>Можешь переписать этот код на C++?</p>
<pre><code class="language-python">a = [0, 1, &quot;привет&quot;, &quot;мир&quot;]
print(a[2], a[3])
</code></pre>
<hr />
<h2>ChatGPT:</h2>
<p>Да, я могу переписать этот код на C++:</p>
<pre><code class="language-cpp">#include &lt;iostream&gt;
#include &lt;vector&gt;

int main() {
    std::vector&lt;std::string&gt; a = { &quot;0&quot;, &quot;1&quot;, &quot;привет&quot;, &quot;мир&quot; };
    std::cout &lt;&lt; a[2] &lt;&lt; &quot; &quot; &lt;&lt; a[3] &lt;&lt; std::endl;
    return 0;
}
</code></pre>
<p>Здесь я использовал std::vector, чтобы создать массив строк, 
поскольку C++ не поддерживает нетипизированные массивы.</p>