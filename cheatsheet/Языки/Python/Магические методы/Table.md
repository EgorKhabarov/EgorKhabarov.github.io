<h1>Арифметические операции</h1>
<table>
<thead>
<tr>
<th>Функция</th>
<th>Пример</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td>def &#95;&#95;eq&#95;&#95;(self, other) -&gt; bool:</td>
<td>self == other</td>
<td>Равенство</td>
</tr>
<tr>
<td>def &#95;&#95;ge&#95;&#95;(self, other) -&gt; bool:</td>
<td>self &gt;= other</td>
<td>Больше или равен</td>
</tr>
<tr>
<td>def &#95;&#95;gt&#95;&#95;(self, other) -&gt; bool:</td>
<td>self &gt; other</td>
<td>Больше</td>
</tr>
<tr>
<td>def &#95;&#95;le&#95;&#95;(self, other) -&gt; bool:</td>
<td>self &lt;= other</td>
<td>Mеньше или равен</td>
</tr>
<tr>
<td>def &#95;&#95;lt&#95;&#95;(self, other) -&gt; bool:</td>
<td>self &lt; other</td>
<td>Меньше</td>
</tr>
<tr>
<td>def &#95;&#95;ne&#95;&#95;(self, other) -&gt; bool:</td>
<td>self != other</td>
<td>Не равен</td>
</tr>
<tr>
<td>def &#95;&#95;or&#95;&#95;(self, other):</td>
<td>self | other</td>
<td>Побитовое ИЛИ</td>
</tr>
<tr>
<td>def &#95;&#95;add&#95;&#95;(self, other):</td>
<td>self + other</td>
<td>Сложение</td>
</tr>
<tr>
<td>def &#95;&#95;and&#95;&#95;(self, other):</td>
<td>self &amp; other</td>
<td>Побитовое И</td>
</tr>
<tr>
<td>def &#95;&#95;ior&#95;&#95;(self, other):</td>
<td>self |= other</td>
<td>Побитовое ИЛИ с присваиванием</td>
</tr>
<tr>
<td>def &#95;&#95;mod&#95;&#95;(self, other):</td>
<td>self % other</td>
<td>Остаток от деления</td>
</tr>
<tr>
<td>def &#95;&#95;mul&#95;&#95;(self, other):</td>
<td>self * other</td>
<td>Умножение</td>
</tr>
<tr>
<td>def &#95;&#95;ror&#95;&#95;(self, other):</td>
<td>self | other</td>
<td>Побитовое ИЛИ с обратным присваиванием</td>
</tr>
<tr>
<td>def &#95;&#95;sub&#95;&#95;(self, other):</td>
<td>self - other</td>
<td>Вычитание</td>
</tr>
<tr>
<td>def &#95;&#95;xor&#95;&#95;(self, other):</td>
<td>self ^ other</td>
<td>Побитовое ИСКЛЮЧАЮЩЕЕ ИЛИ</td>
</tr>
<tr>
<td>def &#95;&#95;iadd&#95;&#95;(self, other):</td>
<td>self += other</td>
<td>Сложение с присваиванием</td>
</tr>
<tr>
<td>def &#95;&#95;iand&#95;&#95;(self, other):</td>
<td>self &amp;= other</td>
<td>Побитовое И с присваиванием</td>
</tr>
<tr>
<td>def &#95;&#95;idiv&#95;&#95;(self, other):</td>
<td>self /= other</td>
<td>Деление с присваиванием</td>
</tr>
<tr>
<td>def &#95;&#95;imod&#95;&#95;(self, other):</td>
<td>self %= other</td>
<td>Взятие остатка от деления с присваиванием</td>
</tr>
<tr>
<td>def &#95;&#95;imul&#95;&#95;(self, other):</td>
<td>self *= other</td>
<td>Умножение с присваиванием</td>
</tr>
<tr>
<td>def &#95;&#95;ipow&#95;&#95;(self, other):</td>
<td>self **= other</td>
<td>Возведение в степень с присваиванием</td>
</tr>
<tr>
<td>def &#95;&#95;isub&#95;&#95;(self, other):</td>
<td>self -= other</td>
<td>Вычитание с присваиванием</td>
</tr>
<tr>
<td>def &#95;&#95;ixor&#95;&#95;(self, other):</td>
<td>self ^= other</td>
<td>Побитовое ИСКЛЮЧАЮЩЕЕ ИЛИ с присваиванием</td>
</tr>
<tr>
<td>def &#95;&#95;radd&#95;&#95;(self, other):</td>
<td>other + self</td>
<td>Сложение справа</td>
</tr>
<tr>
<td>def &#95;&#95;rand&#95;&#95;(self, other):</td>
<td>other &amp; self</td>
<td>Выполняет побитовое И справа</td>
</tr>
<tr>
<td>def &#95;&#95;rdiv&#95;&#95;(self, other):</td>
<td>other / self</td>
<td>Деление справа</td>
</tr>
<tr>
<td>def &#95;&#95;divmod&#95;&#95;(self, other):</td>
<td>divmod(self, other)</td>
<td>Деление с остатком</td>
</tr>
<tr>
<td>def &#95;&#95;rdivmod&#95;&#95;(self, other):</td>
<td>divmod(other, self)</td>
<td>Деление с остатком справа</td>
</tr>
<tr>
<td>def &#95;&#95;rmod&#95;&#95;(self, other):</td>
<td>other % self</td>
<td>Взятие остатка от деления справа</td>
</tr>
<tr>
<td>def &#95;&#95;rmul&#95;&#95;(self, other):</td>
<td>other * self</td>
<td>Умножение справа</td>
</tr>
<tr>
<td>def &#95;&#95;rpow&#95;&#95;(self, other):</td>
<td>other ** self</td>
<td>Возведение в степень справа</td>
</tr>
<tr>
<td>def &#95;&#95;rsub&#95;&#95;(self, other):</td>
<td>other - self</td>
<td>Вычитание справа</td>
</tr>
<tr>
<td>def &#95;&#95;rxor&#95;&#95;(self, other):</td>
<td>other ^ self</td>
<td>Побитовое ИСКЛЮЧАЮЩЕЕ ИЛИ справа</td>
</tr>
<tr>
<td>def &#95;&#95;floordiv&#95;&#95;(self, other):</td>
<td>self // other</td>
<td>Целочисленное деление</td>
</tr>
<tr>
<td>def &#95;&#95;ilshift&#95;&#95;(self, other):</td>
<td>self &lt;&lt;= other</td>
<td>Побитовый сдвиг влево с присваиванием</td>
</tr>
<tr>
<td>def &#95;&#95;imatmul&#95;&#95;(self, other):</td>
<td>self @= other</td>
<td>Матричное умножение с присваиванием</td>
</tr>
<tr>
<td>def &#95;&#95;irshift&#95;&#95;(self, other):</td>
<td>self &gt;&gt;= other</td>
<td>Побитовый сдвиг вправо с присваиванием</td>
</tr>
<tr>
<td>def &#95;&#95;itruediv&#95;&#95;(self, other):</td>
<td>self /= other</td>
<td>Деление с присваиванием</td>
</tr>
<tr>
<td>def &#95;&#95;rlshift&#95;&#95;(self, other):</td>
<td>other &lt;&lt; self</td>
<td>Побитовый сдвиг влево справа</td>
</tr>
<tr>
<td>def &#95;&#95;rmatmul&#95;&#95;(self, other):</td>
<td>other @ self</td>
<td>Матричное умножение справа</td>
</tr>
<tr>
<td>def &#95;&#95;matmul&#95;&#95;(self, other):</td>
<td>self @ other</td>
<td>Матричное умножение</td>
</tr>
<tr>
<td>def &#95;&#95;rrshift&#95;&#95;(self, other):</td>
<td>other &gt;&gt; self</td>
<td>Побитовый сдвиг вправо справа</td>
</tr>
<tr>
<td>def &#95;&#95;rtruediv&#95;&#95;(self, other):</td>
<td>other / self</td>
<td>Деление справа</td>
</tr>
<tr>
<td>def &#95;&#95;truediv&#95;&#95;(self, other):</td>
<td>self / other</td>
<td>Деление</td>
</tr>
<tr>
<td>def &#95;&#95;lshift&#95;&#95;(self, other):</td>
<td>self &lt;&lt; other</td>
<td>Побитовый сдвиг влево</td>
</tr>
<tr>
<td>def &#95;&#95;rshift&#95;&#95;(self, other):</td>
<td>self &gt;&gt; other</td>
<td>Побитовый сдвиг вправо</td>
</tr>
<tr>
<td>def &#95;&#95;ifloordiv&#95;&#95;(self, other):</td>
<td>self //= other</td>
<td>Целочисленное деление с присваиванием</td>
</tr>
<tr>
<td>def &#95;&#95;rfloordiv&#95;&#95;(self, other):</td>
<td>other // self</td>
<td>Целочисленное деление справа</td>
</tr>
<tr>
<td>def &#95;&#95;pos&#95;&#95;(self):</td>
<td>+self</td>
<td>Положительное значение объекта</td>
</tr>
<tr>
<td>def &#95;&#95;neg&#95;&#95;(self):</td>
<td>-self</td>
<td>Отрицательное значение объекта</td>
</tr>
<tr>
<td>def &#95;&#95;invert&#95;&#95;(self):</td>
<td>~self</td>
<td>Инвертированное значение объекта</td>
</tr>
</tbody>
</table>
<h1>func call</h1>
<table>
<thead>
<tr>
<th>Функция</th>
<th>Пример</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td>def &#95;&#95;pow&#95;&#95;(self, power, modulo=None):</td>
<td>pow(self, power, modulo)</td>
<td>Возведение в степень</td>
</tr>
<tr>
<td>def &#95;&#95;abs&#95;&#95;(self):</td>
<td>abs(self)</td>
<td>Абсолютное значение объекта</td>
</tr>
<tr>
<td>def &#95;&#95;hex&#95;&#95;(self):</td>
<td>hex(self)</td>
<td>Строковое представление объекта в<br>шестнадцатеричной системе счисления</td>
</tr>
<tr>
<td>def &#95;&#95;float&#95;&#95;(self):</td>
<td>float(self)</td>
<td>Представление объекта в виде числа с плавающей запятой</td>
</tr>
<tr>
<td>def &#95;&#95;bytes&#95;&#95;(self):</td>
<td>bytes(self)</td>
<td>Байтовое представление объекта</td>
</tr>
<tr>
<td>def &#95;&#95;long&#95;&#95;(self):</td>
<td>int(self)</td>
<td>Длинное целочисленное представление объекта</td>
</tr>
<tr>
<td>def &#95;&#95;int&#95;&#95;(self):</td>
<td>int(self)</td>
<td>Целочисленное представление объекта</td>
</tr>
<tr>
<td>def &#95;&#95;bool&#95;&#95;(self) -&gt; bool:</td>
<td>bool(self)</td>
<td>Булево значение</td>
</tr>
<tr>
<td>def &#95;&#95;oct&#95;&#95;(self):</td>
<td>oct(self)</td>
<td>Строковое представление объекта в<br>восьмеричной системе счисления</td>
</tr>
<tr>
<td>def &#95;&#95;len&#95;&#95;(self):</td>
<td>len(self)</td>
<td>Возвращает длину объекта</td>
</tr>
<tr>
<td>def &#95;&#95;str&#95;&#95;(self):</td>
<td>str(self)</td>
<td>Строковое представление объекта</td>
</tr>
<tr>
<td>def &#95;&#95;hash&#95;&#95;(self):</td>
<td>hash(self)</td>
<td>Хеш-значение объекта</td>
</tr>
<tr>
<td>def &#95;&#95;iter&#95;&#95;(self):</td>
<td>iter(self)</td>
<td>Итератор объекта</td>
</tr>
<tr>
<td>def &#95;&#95;next&#95;&#95;(self):</td>
<td>next(self)</td>
<td>Следующий элемент в итерации</td>
</tr>
<tr>
<td>def &#95;&#95;round&#95;&#95;(self, n=None):</td>
<td>round(self, n)</td>
<td>Округленное значение</td>
</tr>
<tr>
<td>def &#95;&#95;complex&#95;&#95;(self):</td>
<td>complex(self)</td>
<td>Комплексное представление</td>
</tr>
<tr>
<td>def &#95;&#95;reversed&#95;&#95;(self):</td>
<td>reversed(self)</td>
<td>Возвращает обратный итератор объекта</td>
</tr>
<tr>
<td>def &#95;&#95;unicode&#95;&#95;(self):</td>
<td>unicode(self)</td>
<td>Строковое представление объекта (Python 2)</td>
</tr>
<tr>
<td>def &#95;&#95;instancecheck&#95;&#95;(self, instance) -&gt; bool:</td>
<td>isinstance(obj, cls)</td>
<td>Проверяет, является ли объект экземпляром класса</td>
</tr>
<tr>
<td>def &#95;&#95;subclasscheck&#95;&#95;(self, subclass) -&gt; bool:</td>
<td>issubclass(subclass, cls)</td>
<td>Является ли класс подклассом другого класса</td>
</tr>
<tr>
<td>def &#95;&#95;call&#95;&#95;(self, <em>args, </em>*kwargs):</td>
<td>self(<em>args, </em>*kwargs)</td>
<td>Вызывает объект как функцию</td>
</tr>
<tr>
<td>def &#95;&#95;repr&#95;&#95;(self):</td>
<td>repr(self)</td>
<td>Строковое представление объекта</td>
</tr>
<tr>
<td>def &#95;&#95;subclasshook&#95;&#95;(cls, &#95;&#95;subclass):</td>
<td>issubclass(Subclass, MyClass)</td>
<td>Проверяет, является ли класс подклассом другого класса</td>
</tr>
<tr>
<td>def &#95;&#95;dir&#95;&#95;(self):</td>
<td>dir(self)</td>
<td>Список атрибутов и методов объекта</td>
</tr>
<tr>
<td>def &#95;&#95;format&#95;&#95;(self, format_spec):</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="s2">&quot;{0:</span><span class="si">{format_spec}</span><span class="s2">}&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span><br></pre></div></pre></div></div></td>
<td>Форматированную строку объекта</td>
</tr>
<tr>
<td>def &#95;&#95;cmp&#95;&#95;(self, other) -&gt; int:</td>
<td>cmp(self, other)</td>
<td>Сравнивает объекты и возвращает -1, 0 или 1</td>
</tr>
<tr>
<td>def &#95;&#95;aiter&#95;&#95;(self):</td>
<td>awaitable.&#95;&#95;aiter&#95;&#95;()</td>
<td>Асинхронный итератор объекта</td>
</tr>
<tr>
<td>def &#95;&#95;anext&#95;&#95;(self):</td>
<td>awaitable.&#95;&#95;anext&#95;&#95;()</td>
<td>Возвращает следующий элемент в асинхронной итерации</td>
</tr>
<tr>
<td>def &#95;&#95;coerce&#95;&#95;(self, other):</td>
<td>coerce(self, other)</td>
<td>Преобразует объект к общему типу с другим объектом</td>
</tr>
<tr>
<td>def &#95;&#95;index&#95;&#95;(self):</td>
<td>operator.index(self)</td>
<td>Целочисленное представление объекта<br>для использования в индексации</td>
</tr>
<tr>
<td>def &#95;&#95;floor&#95;&#95;(self):</td>
<td>math.floor(self)</td>
<td>Наибольшее целое число, меньшее или равное объекту</td>
</tr>
<tr>
<td>def &#95;&#95;trunc&#95;&#95;(self):</td>
<td>math.trunc(self)</td>
<td>Усеченное значение объекта</td>
</tr>
<tr>
<td>def &#95;&#95;ceil&#95;&#95;(self):</td>
<td>math.ceil(self)</td>
<td>Наименьшее целое число, большее или равное объекту</td>
</tr>
<tr>
<td>def &#95;&#95;copy&#95;&#95;(self):</td>
<td>copy.copy(self)</td>
<td>Создает поверхностную копию объекта</td>
</tr>
<tr>
<td>def &#95;&#95;deepcopy&#95;&#95;(self, memodict={}):</td>
<td>copy.deepcopy(self)</td>
<td>Создает глубокую копию объекта</td>
</tr>
<tr>
<td>def &#95;&#95;sizeof&#95;&#95;(self):</td>
<td>sys.getsizeof(self)</td>
<td>Возвращает размер объекта в байтах</td>
</tr>
<tr>
<td>def &#95;&#95;fspath&#95;&#95;(self):</td>
<td>os.fspath(self)</td>
<td>Возвращает строковое представление<br>объекта для использования в функции fspath</td>
</tr>
</tbody>
</table>
<h1>Контейнеры</h1>
<table>
<thead>
<tr>
<th>Функция</th>
<th>Пример</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td>def &#95;&#95;getitem&#95;&#95;(self, item):</td>
<td>self[item]</td>
<td>Элемент по индексу или ключу</td>
</tr>
<tr>
<td>def &#95;&#95;missing&#95;&#95;(self, key):</td>
<td>self[key]</td>
<td>Вызывается при отсутствии ключа в объекте</td>
</tr>
<tr>
<td>def &#95;&#95;contains&#95;&#95;(self, item) -&gt; bool:</td>
<td>item in self</td>
<td>Содержится ли элемент в объекте</td>
</tr>
<tr>
<td>def &#95;&#95;setslice&#95;&#95;(self, i, j, sequence):</td>
<td>self[i:j] = sequence</td>
<td>Заменяет срез объекта указанной последовательностью</td>
</tr>
<tr>
<td>def &#95;&#95;delattr&#95;&#95;(self, item):</td>
<td>del self.item</td>
<td>Удаляет атрибут объекта</td>
</tr>
<tr>
<td>def &#95;&#95;delitem&#95;&#95;(self, key):</td>
<td>del self[key]</td>
<td>Удаляет элемент по ключу</td>
</tr>
<tr>
<td>def &#95;&#95;delslice&#95;&#95;(self, i, j):</td>
<td>del self[i:j]</td>
<td>Удаляет срез из объекта</td>
</tr>
<tr>
<td>def &#95;&#95;get&#95;&#95;(self, instance, owner):</td>
<td>value = self.&#95;&#95;get&#95;&#95;(instance, owner)</td>
<td>Возвращает значение атрибута объекта в классе-дескрипторе</td>
</tr>
</tbody>
</table>
<h1>Классы</h1>
<table>
<thead>
<tr>
<th>Функция</th>
<th>Пример</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td>def &#95;&#95;new&#95;&#95;(cls, <em>args, </em>*kwargs):</td>
<td>instance = MyClass(args)</td>
<td>Создает новый обьект</td>
</tr>
<tr>
<td>def &#95;&#95;init&#95;&#95;(self):</td>
<td>instance = MyClass(args)</td>
<td>При инициализации нового экземпляра объекта</td>
</tr>
<tr>
<td>def &#95;&#95;class&#95;&#95;(self):</td>
<td>obj_class = obj.&#95;&#95;class&#95;&#95;()</td>
<td>Возвращает класс объекта</td>
</tr>
<tr>
<td>def &#95;&#95;del&#95;&#95;(self):</td>
<td>del self</td>
<td>При удалении объекта</td>
</tr>
<tr>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="nd">@classmethod</span><br><span class="k">def</span> <span class="fm">&#95;&#95;prepare&#95;&#95;</span><span class="p">(</span><span class="n">metacls</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">bases</span><span class="p">):</span><br></pre></div></pre></div></div></td>
<td>metacls.&#95;&#95;prepare&#95;&#95;(name, bases)</td>
<td>Словарь для использования в качестве<br>пространства имен класса</td>
</tr>
<tr>
<td>def &#95;&#95;delete&#95;&#95;(self, instance):</td>
<td>del instance.self</td>
<td>Удаляет атрибут объекта</td>
</tr>
<tr>
<td>def &#95;&#95;init_subclass&#95;&#95;(cls, **kwargs):</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">Subclass</span><span class="p">(</span><span class="n">Parent</span><span class="p">):</span><br>    <span class="k">pass</span><br><span class="n">Subclass</span><span class="o">.</span><span class="n">&#95;&#95;init_subclass&#95;&#95;</span><span class="p">()</span><br></pre></div></pre></div></div></td>
<td>Вызывается при создании подкласса</td>
</tr>
<tr>
<td>def &#95;&#95;mro_entries&#95;&#95;(self, bases):</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">MyClass</span><span class="p">(</span><span class="n">Base1</span><span class="p">,</span> <span class="n">Base2</span><span class="p">,</span> <span class="n">metaclass</span><span class="o">=</span><span class="n">MyMeta</span><span class="p">):</span><br>    <span class="k">pass</span><br><span class="n">MyClass</span><span class="o">.</span><span class="n">&#95;&#95;mro_entries&#95;&#95;</span><span class="p">(</span><span class="n">bases</span><span class="p">)</span><br></pre></div></pre></div></div></td>
<td>Возвращает кортеж для обновления MRO<br>(Method Resolution Order)</td>
</tr>
<tr>
<td>def &#95;&#95;getinitargs&#95;&#95;(self):</td>
<td>args = self.&#95;&#95;getinitargs&#95;&#95;()</td>
<td>Кортеж аргументов для использования при создании объекта</td>
</tr>
<tr>
<td>def &#95;&#95;set_name&#95;&#95;(self, owner, name):</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">MyClass</span><span class="p">:</span><br>    <span class="n">attr</span> <span class="o">=</span> <span class="n">MyDescriptor</span><span class="p">()</span><br><span class="n">MyClass</span><span class="o">.</span><span class="n">attr</span><span class="o">.</span><span class="n">&#95;&#95;set_name&#95;&#95;</span><span class="p">(</span><span class="n">MyClass</span><span class="p">,</span> <span class="s1">&#39;attr&#39;</span><span class="p">)</span><br></pre></div></pre></div></div></td>
<td>Вызывается при установке имени атрибута в классе</td>
</tr>
<tr>
<td>def &#95;&#95;getnewargs&#95;&#95;(self):</td>
<td>args = self.&#95;&#95;getnewargs&#95;&#95;()</td>
<td>Возвращает аргументы для использования<br>при создании нового экземпляра объекта</td>
</tr>
<tr>
<td>def &#95;&#95;getattribute&#95;&#95;(self, item):</td>
<td>value = self.&#95;&#95;getattribute&#95;&#95;('attr')</td>
<td>Возвращает значение атрибута объекта</td>
</tr>
<tr>
<td>def &#95;&#95;getattr&#95;&#95;(self, item):</td>
<td>value = self.&#95;&#95;getattr&#95;&#95;('attr')</td>
<td>Вызывается при обращении<br>к несуществующему атрибуту объекта</td>
</tr>
<tr>
<td>def &#95;&#95;await&#95;&#95;(self):</td>
<td>await awaitable</td>
<td>Возвращает объект, поддерживающий асинхронное ожидание</td>
</tr>
<tr>
<td>def &#95;&#95;set&#95;&#95;(self, instance, value):</td>
<td>instance.attr = value</td>
<td>Устанавливает значение атрибута в экземпляре класса</td>
</tr>
<tr>
<td>def &#95;&#95;class_getitem&#95;&#95;(cls, item):</td>
<td>item_type = MyGenericClass.&#95;&#95;class_getitem&#95;&#95;(Item)</td>
<td>Обобщенный тип объекта</td>
</tr>
<tr>
<td>def &#95;&#95;setattr&#95;&#95;(self, key, value):</td>
<td>self.key = value</td>
<td>Устанавливает значение атрибута объекта</td>
</tr>
<tr>
<td>def &#95;&#95;setitem&#95;&#95;(self, key, value):</td>
<td>self[key] = value</td>
<td>Устанавливает значение элемента по ключу в объекте</td>
</tr>
</tbody>
</table>
<h1>with as</h1>
<table>
<thead>
<tr>
<th>Функция</th>
<th>Пример</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td>def &#95;&#95;enter&#95;&#95;(self):</td>
<td>with self as x:</td>
<td>Выполняет код при входе в блок with</td>
</tr>
<tr>
<td>def &#95;&#95;aenter&#95;&#95;(self):</td>
<td>async with self as x:</td>
<td>Вызывается при входе в асинхронный<br>контекстный блок</td>
</tr>
<tr>
<td>def &#95;&#95;aexit&#95;&#95;(self, exc_type, exc_val, exc_tb):</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="k">async</span> <span class="k">with</span> <span class="bp">self</span> <span class="k">as</span> <span class="n">x</span><span class="p">:</span><br>    <span class="k">pass</span><br><span class="k">await</span> <span class="bp">self</span><span class="o">.</span><span class="fm">&#95;&#95;aexit&#95;&#95;</span><span class="p">(</span><span class="n">exc_type</span><span class="p">,</span> <span class="n">exc_val</span><span class="p">,</span> <span class="n">exc_tb</span><span class="p">)</span><br></pre></div></pre></div></div></td>
<td>Вызывается при выходе из асинхронного контекстного блока</td>
</tr>
<tr>
<td>def &#95;&#95;exit&#95;&#95;(self, exc_type, exc_val, exc_tb):</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="k">with</span> <span class="bp">self</span> <span class="k">as</span> <span class="n">x</span><span class="p">:</span><br>    <span class="k">pass</span><br><span class="bp">self</span><span class="o">.</span><span class="fm">&#95;&#95;exit&#95;&#95;</span><span class="p">(</span><span class="n">exc_type</span><span class="p">,</span> <span class="n">exc_val</span><span class="p">,</span> <span class="n">exc_tb</span><span class="p">)</span><br></pre></div></pre></div></div></td>
<td>Вызывается при выходе из контекстного блока</td>
</tr>
</tbody>
</table>
<h1>Итераторы</h1>
<table>
<thead>
<tr>
<th>Функция</th>
<th>Пример</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<h1>Pickle</h1>
<table>
<thead>
<tr>
<th>Функция</th>
<th>Пример</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td>def &#95;&#95;setstate&#95;&#95;(self, state):</td>
<td>obj.&#95;&#95;setstate&#95;&#95;(state)</td>
<td>Восстанавливает состояние объекта</td>
</tr>
<tr>
<td>def &#95;&#95;reduce_ex&#95;&#95;(self, protocol):</td>
<td>pickle.loads(pickle.dumps(self, protocol))</td>
<td>Возвращает данные для использования в процессе<br>сериализации объекта с протоколом</td>
</tr>
<tr>
<td>def &#95;&#95;getstate&#95;&#95;(self):</td>
<td>pickle.loads(pickle.dumps(self).&#95;&#95;getstate&#95;&#95;())</td>
<td>Возвращает состояние объекта для использования<br>в процессе сериализации</td>
</tr>
<tr>
<td>def &#95;&#95;reduce&#95;&#95;(self):</td>
<td>pickle.loads(pickle.dumps(self))</td>
<td>Возвращает данные для использования<br>в процессе сериализации объекта</td>
</tr>
</tbody>
</table>