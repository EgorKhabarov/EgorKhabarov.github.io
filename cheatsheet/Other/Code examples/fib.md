<pre><code class="language-python">def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
</code></pre>
<pre><code class="language-pycon">&gt;&gt;&gt; print(list(fib(10)))
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
</code></pre>