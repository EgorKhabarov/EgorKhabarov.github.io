<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code160b" onclick="copyCode(code160, code160b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code160"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">PIL</span> <span class="kn">import</span> <span class="n">Image</span>
<span class="kn">from</span> <span class="nn">PIL.ImageDraw</span> <span class="kn">import</span> <span class="n">Draw</span>

<span class="n">image</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="sa">r</span><span class="s2">&quot;&quot;</span><span class="p">)</span>
<span class="n">draw</span> <span class="o">=</span> <span class="n">ImageDraw</span><span class="o">.</span><span class="n">Draw</span><span class="p">(</span><span class="n">image</span><span class="p">)</span>
<span class="n">draw</span> <span class="o">=</span> <span class="n">Draw</span><span class="p">(</span><span class="n">image</span><span class="p">)</span>
</pre></div></div></div>

<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code161b" onclick="copyCode(code161, code161b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code161"><div class="highlight"><pre><span></span><span class="p">[</span><span class="nb">print</span><span class="p">(</span><span class="n">x</span><span class="p">)</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">dir</span><span class="p">(</span><span class="n">draw</span><span class="p">)]</span>
</pre></div></div></div>

<p>arc                 Рисует дугу (часть 'пончика') на изображении. 
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