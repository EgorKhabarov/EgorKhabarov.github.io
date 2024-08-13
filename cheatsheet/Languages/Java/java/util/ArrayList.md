<pre><code class="language-java">import java.util.ArrayList;

public class ArrayListExample {
    public static void main(String[] args) {
        ArrayList&lt;String&gt; list = new ArrayList&lt;&gt;();
        list.add(&quot;Apple&quot;);
        list.add(&quot;Banana&quot;);
        list.add(&quot;Cherry&quot;);

        for (String fruit : list) {
            System.out.println(fruit);
        }
    }
}
</code></pre>