<pre><code class="language-java">import java.util.LinkedList;

public class LinkedListExample {
    public static void main(String[] args) {
        LinkedList&lt;String&gt; list = new LinkedList&lt;&gt;();
        list.add(&quot;Red&quot;);
        list.add(&quot;Green&quot;);
        list.add(&quot;Blue&quot;);

        for (String color : list) {
            System.out.println(color);
        }
    }
}
</code></pre>