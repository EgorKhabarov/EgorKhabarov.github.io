<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">Image</span>
<span class="kn">from</span> <span class="nn">PIL.ImageDraw</span> <span class="kn">import</span> <span class="n">Draw</span>

<span class="n">image</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="sa">r</span><span class="s2">&quot;&quot;</span><span class="p">)</span>
<span class="n">draw</span> <span class="o">=</span> <span class="n">ImageDraw</span><span class="o">.</span><span class="n">Draw</span><span class="p">(</span><span class="n">image</span><span class="p">)</span>
<span class="n">draw</span> <span class="o">=</span> <span class="n">Draw</span><span class="p">(</span><span class="n">image</span><span class="p">)</span>
</pre></div></div></div>

<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="p">[</span><span class="nb">print</span><span class="p">(</span><span class="n">x</span><span class="p">)</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">dir</span><span class="p">(</span><span class="n">draw</span><span class="p">)]</span>
</pre></div></div></div>

<p>arc                 Рисует дугу (часть "пончика") на изображении.
                    Принимает четыре аргумента: координаты прямоугольника, в котором находится дуга, начальный и конечный углы (в градусах), а также цвет линии.</p>
<p>bitmap              Рисует изображение в виде битовой карты на текущем изображении.
                    Принимает два аргумента: координаты верхнего левого угла и изображение в формате Bitmap.</p>
<p>chord               Рисует сегмент круга на изображении, соединяя начальную и конечную точки с центром.
                    Принимает аргументы, аналогичные arc.</p>
<p>draw                Используется для рисования на изображении с помощью кисти.
                    Принимает два аргумента: изображение и цвет кисти.</p>
<p>ellipse             Рисует эллипс на изображении.
                    Принимает два аргумента: координаты прямоугольника, в котором находится эллипс, и цвет линии.</p>
<p>fill                Заполняет область на изображении определенным цветом.
                    Принимает два аргумента: координаты прямоугольника и цвет.</p>
<p>font                Используется для настройки шрифта, который будет использоваться при отрисовке текста.
                    Принимает аргумент в формате ImageFont. (не работало...)</p>
<p>fontmode            Задает режим отображения текста. Может принимать значения "1" или "L".</p>
<p>getfont             Возвращает текущий шрифт.</p>
<p>im                  Текущее изображение.</p>
<p>ink                 Цвет, используемый для рисования.</p>
<p>line                Рисует линию на изображении.
                    Принимает два аргумента: координаты начальной и конечной точек и цвет линии.</p>
<p>mode                Режим изображения.
                    Может принимать значения "1", "L", "P", "RGB" или "CMYK".</p>
<p>multiline_text      Рисует многострочный текст на изображении.
                    Принимает три аргумента: координаты верхнего левого угла, текст и дополнительные параметры.</p>
<p>multiline_textbbox  Возвращает ограничивающий прямоугольник для многострочного текста.
                    Принимает те же аргументы, что и multiline_text.</p>
<p>multiline_textsize  Возвращает размер многострочного текста.
                    Принимает те же аргументы, что и multiline_text.</p>
<p>palette             Палитра изображения.</p>
<p>pieslice            Рисует сегмент пирога на изображении.
                    Принимает аргументы, аналогичные arc.</p>
<p>point               Рисует точку на изображении.
                    Принимает аргументы - координаты точки и цвет.</p>
<p>polygon             Рисует многоугольник на изображении.
                    Принимает два аргумента: список координат вершин многоугольника и цвет линии.</p>
<p>rectangle           Рисует прямоугольник на изображении.
                    Принимает два аргумента: координаты прямоугольника и цвет линии.</p>
<p>regular_polygon     Рисует правильный многоугольник на изображении.
                    Принимает три аргумента: центр многоугольника, количество сторон и радиус.</p>
<p>rounded_rectangle   Рисует прямоугольник с закругленными углами на изображении.
                    Принимает аргументы, аналогичные rectangle.</p>
<p>shape               Рисует многоугольник, который может быть заполнен или обведен.
                    Принимает два аргумента: список координат вершин многоугольника и цвет.</p>
<p>text                Рисует текст на изображении.
                    Принимает три аргумента: координаты верхнего левого угла, текст и цвет.</p>
<p>textbbox            Возвращает ограничивающий прямоугольник для текста.
                    Принимает те же аргументы, что и text.</p>
<p>textlength          Возвращает длину текста.
                    Принимает два аргумента: текст и шрифт.</p>
<p>textsize            Возвращает размер текста.
                    Принимает два аргумента: текст и шрифт.</p>