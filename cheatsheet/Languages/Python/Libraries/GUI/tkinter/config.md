<h1>Общие опции для большинства виджетов</h1>
<table>
<thead>
<tr>
<th>Опция</th>
<th>Описание</th>
<th>Пример использования</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>background</code> / <code>bg</code></td>
<td>Цвет фона виджета</td>
<td><code>widget.config(bg="red")</code></td>
</tr>
<tr>
<td><code>foreground</code> / <code>fg</code></td>
<td>Цвет текста или содержимого виджета</td>
<td><code>widget.config(fg="blue")</code></td>
</tr>
<tr>
<td><code>font</code></td>
<td>Шрифт текста виджета</td>
<td><code>widget.config(font=("Arial", 12))</code></td>
</tr>
<tr>
<td><code>height</code></td>
<td>Высота виджета. Может быть в пикселях или в строках (для текстовых виджетов)</td>
<td><code>widget.config(height=2)</code></td>
</tr>
<tr>
<td><code>width</code></td>
<td>Ширина виджета. Может быть в пикселях или в символах (для текстовых виджетов)</td>
<td><code>widget.config(width=20)</code></td>
</tr>
<tr>
<td><code>padx</code></td>
<td>Внутренний отступ по горизонтали (в пикселях)</td>
<td><code>widget.config(padx=10)</code></td>
</tr>
<tr>
<td><code>pady</code></td>
<td>Внутренний отступ по вертикали (в пикселях)</td>
<td><code>widget.config(pady=5)</code></td>
</tr>
<tr>
<td><code>relief</code></td>
<td>Стиль границы виджета: <code>flat</code>, <code>sunken</code>, <code>raised</code>, <code>groove</code>, <code>ridge</code></td>
<td><code>widget.config(relief="sunken")</code></td>
</tr>
<tr>
<td><code>cursor</code></td>
<td>Курсор, который отображается при наведении на виджет</td>
<td><code>widget.config(cursor="hand2")</code></td>
</tr>
<tr>
<td><code>state</code></td>
<td>Состояние виджета: <code>normal</code>, <code>disabled</code>, <code>active</code></td>
<td><code>widget.config(state="disabled")</code></td>
</tr>
<tr>
<td><code>takefocus</code></td>
<td>Указывает, может ли виджет принимать фокус при перемещении по элементам интерфейса с клавиатуры</td>
<td><code>widget.config(takefocus=True)</code></td>
</tr>
</tbody>
</table>
<h2>Button, Checkbutton, Radiobutton, Label</h2>
<table>
<thead>
<tr>
<th>Опция</th>
<th>Описание</th>
<th>Пример использования</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>text</code></td>
<td>Текст, отображаемый на виджете</td>
<td><code>button.config(text="Click me")</code></td>
</tr>
<tr>
<td><code>image</code></td>
<td>Изображение, отображаемое на виджете</td>
<td><code>button.config(image=my_image)</code></td>
</tr>
<tr>
<td><code>compound</code></td>
<td>Расположение текста относительно изображения: <code>top</code>, <code>bottom</code>, <code>left</code>, <code>right</code>, <code>center</code></td>
<td><code>button.config(compound="left")</code></td>
</tr>
<tr>
<td><code>command</code></td>
<td>Функция, вызываемая при нажатии на кнопку</td>
<td><code>button.config(command=my_function)</code></td>
</tr>
<tr>
<td><code>justify</code></td>
<td>Выравнивание текста: <code>left</code>, <code>center</code>, <code>right</code></td>
<td><code>label.config(justify="left")</code></td>
</tr>
</tbody>
</table>
<h2>Entry</h2>
<table>
<thead>
<tr>
<th>Опция</th>
<th>Описание</th>
<th>Пример использования</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>show</code></td>
<td>Замена вводимых символов на указанный символ (например, для паролей)</td>
<td><code>entry.config(show="*")</code></td>
</tr>
<tr>
<td><code>validate</code></td>
<td>Тип валидации: <code>focus</code>, <code>focusin</code>, <code>focusout</code>, <code>key</code>, или <code>none</code></td>
<td><code>entry.config(validate="key")</code></td>
</tr>
<tr>
<td><code>validatecommand</code></td>
<td>Функция, вызываемая при валидации ввода</td>
<td><code>entry.config(validatecommand=my_validation)</code></td>
</tr>
<tr>
<td><code>invalidcommand</code></td>
<td>Функция, вызываемая при неудачной валидации</td>
<td><code>entry.config(invalidcommand=my_invalid)</code></td>
</tr>
</tbody>
</table>
<h2>Text</h2>
<table>
<thead>
<tr>
<th>Опция</th>
<th>Описание</th>
<th>Пример использования</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>wrap</code></td>
<td>Определяет перенос текста: <code>none</code>, <code>char</code>, <code>word</code></td>
<td><code>text.config(wrap="word")</code></td>
</tr>
<tr>
<td><code>spacing1</code></td>
<td>Интервал перед первой строкой параграфа (в пикселях)</td>
<td><code>text.config(spacing1=5)</code></td>
</tr>
<tr>
<td><code>spacing2</code></td>
<td>Интервал между строками в параграфе</td>
<td><code>text.config(spacing2=2)</code></td>
</tr>
<tr>
<td><code>spacing3</code></td>
<td>Интервал после последней строки параграфа</td>
<td><code>text.config(spacing3=5)</code></td>
</tr>
<tr>
<td><code>state</code></td>
<td>Состояние виджета: <code>normal</code>, <code>disabled</code></td>
<td><code>text.config(state="disabled")</code></td>
</tr>
</tbody>
</table>
<h2>Listbox</h2>
<table>
<thead>
<tr>
<th>Опция</th>
<th>Описание</th>
<th>Пример использования</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>selectmode</code></td>
<td>Режим выбора элементов: <code>browse</code>, <code>single</code>, <code>multiple</code>, <code>extended</code></td>
<td><code>listbox.config(selectmode="multiple")</code></td>
</tr>
<tr>
<td><code>activestyle</code></td>
<td>Стиль выделения активного элемента: <code>dotbox</code>, <code>underline</code>, <code>none</code></td>
<td><code>listbox.config(activestyle="underline")</code></td>
</tr>
</tbody>
</table>
<h2>Scale</h2>
<table>
<thead>
<tr>
<th>Опция</th>
<th>Описание</th>
<th>Пример использования</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>from_</code></td>
<td>Начальное значение шкалы</td>
<td><code>scale.config(from_=0)</code></td>
</tr>
<tr>
<td><code>to</code></td>
<td>Конечное значение шкалы</td>
<td><code>scale.config(to=100)</code></td>
</tr>
<tr>
<td><code>orient</code></td>
<td>Ориентация шкалы: <code>horizontal</code>, <code>vertical</code></td>
<td><code>scale.config(orient="horizontal")</code></td>
</tr>
<tr>
<td><code>length</code></td>
<td>Длина шкалы (в пикселях)</td>
<td><code>scale.config(length=200)</code></td>
</tr>
<tr>
<td><code>tickinterval</code></td>
<td>Интервал между отметками на шкале</td>
<td><code>scale.config(tickinterval=10)</code></td>
</tr>
<tr>
<td><code>resolution</code></td>
<td>Шаг изменения значения</td>
<td><code>scale.config(resolution=0.1)</code></td>
</tr>
<tr>
<td><code>showvalue</code></td>
<td>Отображать ли текущее значение на шкале: <code>True</code> или <code>False</code></td>
<td><code>scale.config(showvalue=True)</code></td>
</tr>
</tbody>
</table>
<h2>Canvas</h2>
<table>
<thead>
<tr>
<th>Опция</th>
<th>Описание</th>
<th>Пример использования</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>scrollregion</code></td>
<td>Указывает область для прокрутки на холсте</td>
<td><code>canvas.config(scrollregion=(0, 0, 500, 500))</code></td>
</tr>
<tr>
<td><code>xscrollcommand</code></td>
<td>Команда для горизонтальной прокрутки</td>
<td><code>canvas.config(xscrollcommand=x_scroll.set)</code></td>
</tr>
<tr>
<td><code>yscrollcommand</code></td>
<td>Команда для вертикальной прокрутки</td>
<td><code>canvas.config(yscrollcommand=y_scroll.set)</code></td>
</tr>
</tbody>
</table>
<h2>Menu</h2>
<table>
<thead>
<tr>
<th>Опция</th>
<th>Описание</th>
<th>Пример использования</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>tearoff</code></td>
<td>Определяет, можно ли открепить меню</td>
<td><code>menu.config(tearoff=False)</code></td>
</tr>
</tbody>
</table>
<h2>Checkbutton, Radiobutton</h2>
<table>
<thead>
<tr>
<th>Опция</th>
<th>Описание</th>
<th>Пример использования</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>variable</code></td>
<td>Переменная, связанная с состоянием чекбокса/радиокнопки</td>
<td><code>checkbutton.config(variable=var)</code></td>
</tr>
<tr>
<td><code>value</code></td>
<td>Значение, устанавливаемое переменной при выборе кнопки</td>
<td><code>radiobutton.config(value=1)</code></td>
</tr>
<tr>
<td><code>indicatoron</code></td>
<td>Определяет, будет ли отображаться индикатор (круг или квадрат): <code>True</code> или <code>False</code></td>
<td><code>checkbutton.config(indicatoron=False)</code></td>
</tr>
</tbody>
</table>
<h2>Frame</h2>
<table>
<thead>
<tr>
<th>Опция</th>
<th>Описание</th>
<th>Пример использования</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>borderwidth</code></td>
<td>Ширина границы фрейма (в пикселях)</td>
<td><code>frame.config(borderwidth=2)</code></td>
</tr>
<tr>
<td><code>highlightbackground</code></td>
<td>Цвет фона рамки при отсутствии фокуса</td>
<td><code>frame.config(highlightbackground="blue")</code></td>
</tr>
<tr>
<td><code>highlightcolor</code></td>
<td>Цвет рамки при получении фокуса</td>
<td><code>frame.config(highlightcolor="green")</code></td>
</tr>
<tr>
<td><code>highlightthickness</code></td>
<td>Толщина рамки (в пикселях)</td>
<td><code>frame.config(highlightthickness=2)</code></td>
</tr>
</tbody>
</table>
<h3>Пример использования нескольких параметров</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">tkinter</span> <span class="k">as</span> <span class="nn">tk</span>

<span class="n">root</span> <span class="o">=</span> <span class="n">tk</span><span class="o">.</span><span class="n">Tk</span><span class="p">()</span>

<span class="n">button</span> <span class="o">=</span> <span class="n">tk</span><span class="o">.</span><span class="n">Button</span><span class="p">(</span><span class="n">root</span><span class="p">,</span> <span class="n">text</span><span class="o">=</span><span class="s2">&quot;Click me&quot;</span><span class="p">,</span> <span class="n">bg</span><span class="o">=</span><span class="s2">&quot;lightblue&quot;</span><span class="p">,</span> <span class="n">fg</span><span class="o">=</span><span class="s2">&quot;white&quot;</span><span class="p">,</span> <span class="n">font</span><span class="o">=</span><span class="p">(</span><span class="s2">&quot;Arial&quot;</span><span class="p">,</span> <span class="mi">16</span><span class="p">))</span>
<span class="n">button</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="n">padx</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span> <span class="n">pady</span><span class="o">=</span><span class="mi">10</span><span class="p">)</span>

<span class="n">entry</span> <span class="o">=</span> <span class="n">tk</span><span class="o">.</span><span class="n">Entry</span><span class="p">(</span><span class="n">root</span><span class="p">,</span> <span class="n">show</span><span class="o">=</span><span class="s2">&quot;*&quot;</span><span class="p">,</span> <span class="n">font</span><span class="o">=</span><span class="p">(</span><span class="s2">&quot;Courier&quot;</span><span class="p">,</span> <span class="mi">12</span><span class="p">),</span> <span class="n">width</span><span class="o">=</span><span class="mi">30</span><span class="p">)</span>
<span class="n">entry</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="n">padx</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span> <span class="n">pady</span><span class="o">=</span><span class="mi">10</span><span class="p">)</span>

<span class="n">label</span> <span class="o">=</span> <span class="n">tk</span><span class="o">.</span><span class="n">Label</span><span class="p">(</span><span class="n">root</span><span class="p">,</span> <span class="n">text</span>

<span class="o">=</span><span class="s2">&quot;Hello, Tkinter!&quot;</span><span class="p">,</span> <span class="n">relief</span><span class="o">=</span><span class="s2">&quot;sunken&quot;</span><span class="p">,</span> <span class="n">width</span><span class="o">=</span><span class="mi">20</span><span class="p">)</span>
<span class="n">label</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="n">padx</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span> <span class="n">pady</span><span class="o">=</span><span class="mi">10</span><span class="p">)</span>

<span class="n">root</span><span class="o">.</span><span class="n">mainloop</span><span class="p">()</span>
</pre></div></div></div>

<p>Эти параметры помогут тонко настраивать виджеты в интерфейсах на базе <code>Tkinter</code>.</p>