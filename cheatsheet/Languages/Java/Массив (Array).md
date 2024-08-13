<ul>
<li><strong><code>Массив (array)</code></strong> — это структура данных фиксированного размера</li>
<li><strong><code>Список (list)</code></strong> — это интерфейс в Java, который представляет динамическую структуру данных, размер которой может изменяться.</li>
</ul>
<pre><code class="language-java">// Создание пустого массива
char[] stroka;
// Или
int numbers[];
numbers = new int[10];

int[] nums = new int[4];
nums[0] = 1;

int[] nums2 = new int[] { 1, 2, 3, 5 };
int[] nums3 = { 1, 2, 3, 5 };

System.out.println(Arrays.toString(nums3));
System.out.println(nums3.length);

System.out.println(Arrays.toString(new int[] { 1, 2, 3, 5 }));
System.out.println(new int[] { 1, 2, 3, 5 }.length);
</code></pre>
<h1>Вывод значений</h1>
<p>Для вывода всех значений массива используйте метод <code>Arrays.toString()</code>, преобразующий массив в строку.</p>
<pre><code class="language-java">import java.util.Arrays;
</code></pre>
<pre><code class="language-java">System.out.println(Arrays.toString(arr));
</code></pre>
<p>Или напишите цикл, выводящий последовательно элементы массива.</p>
<pre><code class="language-java">for(int i=0; i&lt;arr.length; i++) {
    System.out.println(arr[i]);
}
// Или
for (int el : arr) {
    System.out.println(el);
}
</code></pre>
<h1>Многомерный массив</h1>
<pre><code class="language-java">int[][] x = { { 0, 1, 2 }, { 3, 4, 5 } };
</code></pre>
<p><img alt="collections.jpg" src="Языки/Java/collections.jpg" /></p>
<p>Основные коллекции
Помимо главного интерфейса Collection есть три других главных формата:</p>
<ul>
<li><code>List</code> - коллекция для создания массивов данных, где индексами являются числа (0, 1, 2 и так далее);</li>
<li><code>Set</code> - тоже самое что <code>List</code>, вот только в <code>Set</code> нельзя установить повторяющиеся элементы;</li>
<li><code>Map</code> - коллекция для создания массивов данных, где индексами являются ключи ("one", "2", "three" и так далее).</li>
</ul>
<pre><code class="language-java">import java.util.LinkedList;
import java.util.ArrayList;


public class Main {
    public static void main(String[] args) {
        ArrayList&lt;Float&gt; numbers = new ArrayList&lt;&gt;(1);  // 1 (initialCapacity) можно не указывать
        LinkedList&lt;String&gt; names = new LinkedList&lt;&gt;();
    }
}
</code></pre>
<ul>
<li><code>add()</code> - добавление элемента в конец массива;</li>
<li><code>remove()</code> - удаление элемента из массива по его индексу;</li>
<li><code>clear()</code> - очистка всего массива;</li>
<li><code>size()</code> - получение размера массива (количество элементов);</li>
<li><code>addFirst()</code> - добавление элемента в начало массива;</li>
<li><code>addLast()</code> - добавление элемента в конец;</li>
<li><code>clone()</code> - выполняет клонирование массива;</li>
<li><code>get()</code> - возвращает элемент по индексу;</li>
<li><code>getFirst()</code> - возвращает первый элемент в массиве;</li>
<li><code>getLast()</code> - возвращает последний элемент в массиве;</li>
<li><code>set(index, element)</code> - меняет значение элемента по индексу.</li>
</ul>
<pre><code class="language-java">List&lt;Object&gt; items = new ArrayList&lt;&gt;();
items.add(&quot;Hello&quot;);
items.add(42);
items.add(3.14);
items.add(0, 3.14);
items.add(2, 3.14);

System.out.println(items.get(0));
// System.out.println(items.get(-1)); // Index -1 out of bounds for length 5
System.out.println(items.size());
for (Object item : items) {
    System.out.println(item);
}
</code></pre>
<pre><code class="language-output">5
3.14
Hello
3.14
42
3.14
</code></pre>