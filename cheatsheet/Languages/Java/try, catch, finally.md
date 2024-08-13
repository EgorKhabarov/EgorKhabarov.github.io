<pre><code class="language-java">public class ExceptionExample {
    public static void main(String[] args) {
        try {
            int result = 10 / 0;  // Это вызовет ArithmeticException
        } catch (ArithmeticException e) {
            System.out.println(&quot;Ошибка деления на ноль: &quot; + e.getMessage());
        } finally {
            System.out.println(&quot;Блок finally выполняется всегда.&quot;);
        }
    }
}
</code></pre>
<h1>try-with-resources</h1>
<pre><code class="language-java">try (BufferedReader reader = new BufferedReader(new FileReader(&quot;file.txt&quot;))) {
    String line;
    while ((line = reader.readLine()) != null) {
        System.out.println(line);
    }
} catch (IOException e) {
    e.printStackTrace();
}
</code></pre>
<h2>Без круглых скобочек</h2>
<pre><code class="language-java">BufferedReader reader = null;
try {
    reader = new BufferedReader(new FileReader(&quot;file.txt&quot;));
    String line;
    while ((line = reader.readLine()) != null) {
        System.out.println(line);
    }
} catch (IOException e) {
    e.printStackTrace();
} finally {
    if (reader != null) {
        try {
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
</code></pre>