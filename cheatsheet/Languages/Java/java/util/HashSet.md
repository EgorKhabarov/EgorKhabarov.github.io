<pre><code class="language-java">import java.util.HashSet;

public class HashSetExample {
    public static void main(String[] args) {
        HashSet&lt;String&gt; set = new HashSet&lt;&gt;();
        set.add(&quot;Dog&quot;);
        set.add(&quot;Cat&quot;);
        set.add(&quot;Bird&quot;);

        for (String animal : set) {
            System.out.println(animal);
        }
    }
}
</code></pre>