<pre><code class="language-java">import java.util.HashMap;

public class HashMapExample {
    public static void main(String[] args) {
        HashMap&lt;String, Integer&gt; map = new HashMap&lt;&gt;();
        map.put(&quot;Alice&quot;, 30);
        map.put(&quot;Bob&quot;, 25);
        map.put(&quot;Charlie&quot;, 35);

        for (String name : map.keySet()) {
            System.out.println(name + &quot;: &quot; + map.get(name));
        }
    }
}
</code></pre>