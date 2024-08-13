<p>Библиотека "marshal" в Python используется для сериализации и десериализации объектов.
Она предоставляет функциональность для сохранения объектов в бинарном формате и восстановления их позже.</p>
<p>Методы модуля "marshal" и их краткое описание:
<code>dump(obj, file)</code> - Сериализует объект <code>obj</code> и записывает его в файл <code>file</code>.
<code>load(file)</code> - Читает сериализованные данные из файла <code>file</code> и восстанавливает объект.
<code>dumps(obj)</code> - Возвращает сериализованное представление объекта <code>obj</code> в виде строки.
<code>loads(bytes)</code> - Восстанавливает объект из сериализованного представления, передаваемого в виде строки <code>bytes</code>.
<code>version</code> - Целое число, представляющее версию протокола сериализации.</p>
<p>Наиболее распространенные методы "marshal" и их описание:</p>
<p><code>dump(obj, file)</code> - Сериализует объект <code>obj</code> и записывает его в файл <code>file</code>.</p>
<pre><code class="language-python">import marshal

data = {&quot;name&quot;: &quot;John&quot;, &quot;age&quot;: 30}
with open(&quot;data.bin&quot;, &quot;wb&quot;) as file:
    marshal.dump(data, file)
</code></pre>
<p><code>load(file)</code> - Читает сериализованные данные из файла <code>file</code> и восстанавливает объект.</p>
<pre><code class="language-python">import marshal

with open(&quot;data.bin&quot;, &quot;rb&quot;) as file:
    data = marshal.load(file)
    print(data)  # Вывод: {&quot;name&quot;: &quot;John&quot;, &quot;age&quot;: 30}
</code></pre>
<p><code>dumps(obj)</code> - Возвращает сериализованное представление объекта <code>obj</code> в виде строки.</p>
<pre><code class="language-python">import marshal

data = {&quot;name&quot;: &quot;John&quot;, &quot;age&quot;: 30}
serialized = marshal.dumps(data)
print(serialized)
</code></pre>
<p><code>loads(bytes)</code> - Восстанавливает объект из сериализованного представления, передаваемого в виде строки <code>bytes</code>.</p>
<pre><code class="language-python">import marshal

serialized = (
    b&quot;\x80\x04\x95\x0f\x00\x00\x00\x00\x00\x00\x8c\x08\x00\x00\x00Hello!&quot;
    b&quot;\x94\x8c\x01\x00\x00\x00x\x94\x8c\x01\x00\x00\x00y\x94\x2e\x94\x94&quot;
    b&quot;\x8c\x06\x00\x00\x00result\x94\x94\x8c\x05\x00\x00\x00float\x94\x93\x00\x00\x00\x00\x00\x00\x00.&quot;
)

data = marshal.loads(serialized)
print(data)  # Вывод: {&quot;Hello!&quot;: {&quot;x&quot;: &quot;y&quot;, &quot;result&quot;: None, &quot;float&quot;: 0.0}}
</code></pre>