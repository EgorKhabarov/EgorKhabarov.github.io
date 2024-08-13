<pre><code class="language-python">def quicksort(array):
    if len(array) &lt; 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i &lt;= pivot]
        greater = [i for i in array[1:] if i &gt; pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


quicksortL = lambda array: (
    array
    if len(array) &lt; 2 else
    (
        lambda pivot, less, greater: quicksortL(less) + [pivot] + quicksortL(greater)
    )(
        **(
            lambda pivot, temp_arr: {
                &quot;pivot&quot;: pivot,
                &quot;less&quot;: [i for i in temp_arr if i &lt;= pivot],
                &quot;greater&quot;: [i for i in temp_arr if i &gt; pivot]
            }
        )(array[0], array[1:])
    )
)
</code></pre>
<pre><code class="language-pycon">&gt;&gt;&gt; print(quicksort([10, 5, 2, 3]))
[2, 3, 5, 10]
</code></pre>