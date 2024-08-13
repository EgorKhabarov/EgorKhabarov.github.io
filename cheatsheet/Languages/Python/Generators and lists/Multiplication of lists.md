<pre><code class="language-pycon">&gt;&gt;&gt; a = [[]]*3
&gt;&gt;&gt; for x in a:
...     print(id(x))
...
3276075832448
3276075832448
3276075832448
&gt;&gt;&gt; a[1].append(1)
&gt;&gt;&gt; a
[[1], [1], [1]]
&gt;&gt;&gt;
&gt;&gt;&gt; b = [[] for _ in range(3)]
&gt;&gt;&gt; for x in b:
...     print(id(x))
...
3276075828928
3276075828992
3276075828864
&gt;&gt;&gt; b[1].append(1)
&gt;&gt;&gt; b
[[], [1], []]
&gt;&gt;&gt;
&gt;&gt;&gt; c = [[]]
&gt;&gt;&gt; print(id(c[0]))
3276075894784
&gt;&gt;&gt; for x in (c + c):
...     print(id(x))
...
3276075894784
3276075894784
&gt;&gt;&gt;
&gt;&gt;&gt; d = ((),)*3
&gt;&gt;&gt; for x in d:
...     print(id(d))
...
3276075830656
3276075830656
3276075830656
</code></pre>