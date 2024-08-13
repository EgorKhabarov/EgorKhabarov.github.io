<p>Цикл for
for (начальные_условия;  условие_для_выполнения_цикла; изменение_параметров_цикла) {}</p>
<pre><code class="language-cpp">for(int i = 1; i &lt; 10; i++) {}
</code></pre>
<p>Но можно и так</p>
<pre><code class="language-cpp">int i = 1;
for (; i &lt; 10;) {
    std::cout &lt;&lt; i &lt;&lt; &quot; * &quot; &lt;&lt; i &lt;&lt; &quot; = &quot; &lt;&lt; i * i &lt;&lt; std::endl;
    i++;
}
</code></pre>
<p>Этот цикл применим к контейнерам разной природы (массивам, векторам, спискам и т. д.).
Пока рассмотрим его на примере строк. 
Цикл позволяет удобно проитерироваться по символам строки, не используя индексов. 
В этом примере мы считываем строку и печатаем отдельно все символы строки и их ASCII-коды:</p>
<pre><code class="language-cpp">#include &lt;iostream&gt;
#include &lt;string&gt;

int main() {
    std::string line;
    std::getline(std::cin, line);
    for (char symbol : line) {
        std::cout &lt;&lt; symbol &lt;&lt; &quot;\t&quot; &lt;&lt; static_cast&lt;int&gt;(symbol) &lt;&lt; &quot;\n&quot;;
    }
}
</code></pre>