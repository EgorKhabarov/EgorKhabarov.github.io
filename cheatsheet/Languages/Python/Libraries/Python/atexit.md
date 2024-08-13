<p>Модуль atexit в Python предоставляет возможность регистрации функций,
которые будут выполнены при завершении программы.
Это позволяет управлять завершением программы и выполнением дополнительных действий перед выходом.</p>
<table>
<thead>
<tr>
<th>Метод/Подмодуль</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td>atexit.register(func)</td>
<td>Регистрирует функцию func для выполнения при выходе из программы.</td>
</tr>
</tbody>
</table>
<p><strong>atexit.register(func)</strong> Регистрирует функцию для выполнения при выходе из программы.</p>
<pre><code class="language-python">import atexit

def exit_handler():
    print(&quot;Выход из программы&quot;)

atexit.register(exit_handler)
</code></pre>