<p>Шаблоны функций, а также шаблоны классов в языке C++ это мощные технологии, 
что позволяют создавать шаблонные конструкции и далее при передачи данных передавать как значения, так и типы данных.</p>
<p>Для создания шаблонной функции необходимо использовать ключевое слово template, 
а также в угловых скобках необходимо указывать принимаемый тип данных. 
Можно принимать один или несколько типов данных. </p>
<p>Пример создания шаблонной функции:</p>
<pre><code class="language-cpp">template &lt;typename Type1&gt; // Указываем что это шаблон функции
// Принимаем параметр value и его тип данных мы получим
// также в качестве передаваемого параметра - Type1
void funct (Type1 *value) {
    cout &lt;&lt; value; // Просто выводим это значение
}
</code></pre>
<p>Для передачи нескольких типов данных стоит прописать следующее:</p>
<pre><code class="language-cpp">// Здесь мы получаем сразу два типа данных
template &lt;typename Type1, typename Type2&gt;
void funct (Type1 *value, Type2 *newValue) {
    // Мы можем использовать передаваемые типы в самой функции
    Type1 someNew;
    cout &lt;&lt; newValue; // Просто выводим значение
}
</code></pre>
<p>Для вызова шаблонной функции пропишите следующее:</p>
<pre><code class="language-cpp">// Вызов функции с одним параметром
funct&lt;double&gt;(value);
// Вызов с несколькими параметрами
funct&lt;char, double&gt;(value, oneMoreValue);
</code></pre>
<p>Шаблоны функций</p>
<pre><code class="language-cpp">#include &lt;iostream&gt;

using namespace std;

template &lt;typename T1, typename T2&gt;
T2 printArr (const T1 * array, int i) {
    int count = 0;
    for (int j = 0; j &lt; i; j++) {
        cout &lt;&lt; array[j] &lt;&lt; &quot; &quot;;
        count++;
    }
    cout &lt;&lt; endl;
    return count;
}

int main(int argc, const char * argv[]) {

    const int iSize = 3, fSize = 2, dSize = 3, cSize = 5;

    int i_arr[iSize] = {23, 45, 78};
    float f_arr[fSize] = {12.2, 67.5};
    double d_arr[dSize] = {3.345, 7.567, 9.023};
    char c_arr[cSize] = {&quot;HI!!&quot;};

    cout &lt;&lt; &quot;Массив с типом данных int: &quot;;
    cout &lt;&lt; &quot;Количество элементов: &quot; &lt;&lt; printArr&lt;int, int&gt;(i_arr, iSize) &lt;&lt; endl;
    cout &lt;&lt; &quot;Массив с типом данных float: &quot;;
    cout &lt;&lt; &quot;Количество элементов: &quot; &lt;&lt; printArr&lt;float, int&gt;(f_arr, fSize) &lt;&lt; endl;
    cout &lt;&lt; &quot;Массив с типом данных double: &quot;;
    cout &lt;&lt; &quot;Количество элементов: &quot; &lt;&lt; printArr&lt;double, int&gt;(d_arr, dSize) &lt;&lt; endl;
    cout &lt;&lt; &quot;Массив с типом данных char: &quot;;
    cout &lt;&lt; &quot;Количество элементов: &quot; &lt;&lt; printArr&lt;char, int&gt;(c_arr, cSize) &lt;&lt; endl;

    cin.get();
    return 0;
}
</code></pre>
<p>Обьяснение от ChatGPT:</p>
<p>Шаблоны функций и классов в C++ - это механизм, который позволяет создавать 
универсальные классы и функции, которые могут работать с разными типами данных. 
Вместо того, чтобы создавать отдельную функцию или класс для каждого типа данных, 
вы можете определить шаблон, который может использоваться с разными типами данных.</p>
<p>Определение шаблона функции выглядит так:</p>
<pre><code class="language-cpp">template &lt;typename T&gt;
T max(T a, T b) {
  return (a &gt; b) ? a : b;
}
</code></pre>
<p>В этом примере T является параметром шаблона, который может быть любым типом данных. 
Когда вы вызываете функцию max с разными типами данных, компилятор создает специализированную 
версию функции для каждого типа данных, с которым вы вызываете эту функцию.</p>