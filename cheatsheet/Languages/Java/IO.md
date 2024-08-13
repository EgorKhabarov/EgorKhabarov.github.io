<h2>File</h2>
<pre><code class="language-java">import java.io.File;
import java.io.IOException;

public class FileExample {
    public static void main(String[] args) {
        try {
            File file = new File(&quot;example.txt&quot;);
            if (file.createNewFile()) {
                System.out.println(&quot;Файл создан: &quot; + file.getName());
            } else {
                System.out.println(&quot;Файл уже существует.&quot;);
            }
        } catch (IOException e) {
            System.out.println(&quot;Произошла ошибка: &quot; + e.getMessage());
        }
    }
}
</code></pre>
<h2>BufferedReader</h2>
<pre><code class="language-java">import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class BufferedReaderExample {
    public static void main(String[] args) {
        try (BufferedReader br = new BufferedReader(new FileReader(&quot;example.txt&quot;))) {
            String line;
            while ((line = br.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException e) {
            System.out.println(&quot;Произошла ошибка: &quot; + e.getMessage());
        }
    }
}
</code></pre>
<h2>FileWriter</h2>
<pre><code class="language-java">import java.io.FileWriter;
import java.io.IOException;

public class FileWriterExample {
    public static void main(String[] args) {
        try (FileWriter fw = new FileWriter(&quot;example.txt&quot;)) {
            fw.write(&quot;Hello, world!&quot;);
        } catch (IOException e) {
            System.out.println(&quot;Произошла ошибка: &quot; + e.getMessage());
        }
    }
}
</code></pre>