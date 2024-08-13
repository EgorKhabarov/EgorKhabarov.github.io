<pre><code class="language-java">import java.util.Arrays;
</code></pre>
<pre><code class="language-java">int[] nums = { 1, 2, 3, 5 };
System.out.println(Arrays.toString(nums));
</code></pre>
<p><code>Arrays.copyOf</code> - копирует один массив в другой.</p>
<pre><code class="language-java">int[] arr = new int[] { 1, 2, 3, 5 };
int[] some_new = Arrays.copyOf(arr, arr.length);
</code></pre>
<p><code>Arrays.sort</code> - сортировка массива.</p>
<pre><code class="language-java">int[] numbers = new int[] { 1, 7, 3, 5, 2, 6, 4 };

Arrays.sort(numbers);
</code></pre>