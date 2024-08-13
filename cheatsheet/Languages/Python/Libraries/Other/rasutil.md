<p>Библиотека "rasutil" (raspberry utility) используется для упрощения
разработки и взаимодействия с Raspberry Pi в языке программирования Python.</p>
<p>Таблица методов для модуля "rasutil":
Method 1: GPIOInit() - Инициализирует пины GPIO на Raspberry Pi.
Method 2: GPIOSet(pin, value) - Устанавливает значение пина GPIO на Raspberry Pi.
Method 3: GPIORead(pin) - Считывает значение с пина GPIO на Raspberry Pi.</p>
<p>Методы модуля "rasutil" позволяют управлять GPIO пинами на Raspberry Pi,
инициализировать их, устанавливать значения и считывать значения с этих пинов.</p>
<p>Список самых частых методов и их описания:
GPIOInit() - Инициализирует пины GPIO на Raspberry Pi.</p>
<pre><code class="language-python">rasutil.GPIOInit()
</code></pre>
<p>Этот метод инициализирует пины GPIO на Raspberry Pi перед использованием.</p>
<p>GPIOSet(pin, value) - Устанавливает значение пина GPIO на Raspberry Pi.</p>
<pre><code class="language-python">rasutil.GPIOSet(18, 1)
</code></pre>
<p>Этот метод устанавливает значение 1 на пине GPIO 18 на Raspberry Pi.</p>
<p>GPIORead(pin) - Считывает значение с пина GPIO на Raspberry Pi.</p>
<pre><code class="language-python">value = rasutil.GPIORead(12)
</code></pre>
<p>Этот метод считывает значение с пина GPIO 12 на Raspberry Pi и сохраняет его в переменную "value".</p>
<p>Методы "GPIOSet" и "GPIORead" позволяют управлять значениями пинов GPIO на Raspberry Pi,
устанавливая значения и считывая их соответственно. Метод "GPIOInit" необходим для инициализации пинов GPIO перед их использованием.</p>