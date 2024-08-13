<p>Цикл for в JavaScript используется для выполнения одного 
или нескольких операторов многократно, пока условие в цикле истинно. 
Синтаксис цикла for выглядит следующим образом:</p>
<pre><code class="language-js">for (initialization; condition; final-expression) {
   statement(s)
}
</code></pre>
<p>initialization     выполняется один раз перед началом цикла 
                   и обычно используется для инициализации счетчика цикла.
condition          условие, которое проверяется перед каждой итерацией цикла. 
                   Если условие истинно, то тело цикла выполняется, иначе цикл завершается.
final-expression   выполняется после каждой итерации цикла 
                   и обычно используется для изменения счетчика цикла.
statement(s)       один или несколько операторов, которые выполняются в теле цикла.</p>
<pre><code class="language-js">for (let i = 0; i &lt; 5; i++) {
   console.log(i);
}
</code></pre>
<p>Цикл по списку</p>
<pre><code class="language-js">var myArray = [1, 2, 3, 4, 5];
for (var i = 0; i &lt; myArray.length; i++) {
  console.log(myArray[i]);
}
</code></pre>
<p>или</p>
<pre><code class="language-js">var myArray = [1, 2, 3, 4, 5];
for (const element of myArray) {
  console.log(element);
}
</code></pre>