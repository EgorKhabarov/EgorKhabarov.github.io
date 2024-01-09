<table>
<thead>
<tr>
<th>Флаг</th>
<th>Пример запуска</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td>-c</td>
<td>python -c &lt;код&gt;</td>
<td>Позволяет выполнить однострочный Python-код из командной строки.</td>
</tr>
<tr>
<td>-m</td>
<td>python -m</td>
<td>Позволяет запустить указанный Python-модуль как скрипт.</td>
</tr>
<tr>
<td>-i (или —interactive)</td>
<td>python -i</td>
<td>Флаг -i запускает интерпретатор Python в интерактивном режиме после выполнения скрипта.</td>
</tr>
<tr>
<td>-O (или —optimize)</td>
<td>python -O</td>
<td>Включает режим оптимизации, который удаляет отладочную информацию и выполняет оптимизации в байт-коде.<br>Это может уменьшить размер файлов .pyc и улучшить производительность, но осложнить отладку.</td>
</tr>
<tr>
<td>-B (или —dont-write-bytecode)</td>
<td>python -B</td>
<td>Предотвращает запись байт-кода (.pyc файлов) на диск.</td>
</tr>
<tr>
<td>-v (или —verbose)</td>
<td>python -v</td>
<td>Выводит подробные сообщения о том, какие модули импортируются<br>и какие файлы открываются в процессе выполнения программы.</td>
</tr>
<tr>
<td>-q (или —quiet)</td>
<td>python -q</td>
<td>Уменьшает уровень вывода, игнорируя сообщения о запуске и прочие информационные сообщения.</td>
</tr>
<tr>
<td>-E (или —ignore-environment)</td>
<td>python -E</td>
<td>Игнорировать переменные окружения,<br>которые обычно влияют на поведение Python, такие как PYTHONPATH.</td>
</tr>
<tr>
<td>-u (или —unbuffered)</td>
<td>python -u</td>
<td>Переключает режим не буферизованного ввода/вывода.<br>Полезно при работе с каналами и потоками данных,<br>чтобы гарантировать более немедленную обработку данных.</td>
</tr>
<tr>
<td>-h (или —help)</td>
<td>python -h<br>python —help</td>
<td>Выведет список всех доступных флагов и их описания.</td>
</tr>
</tbody>
</table>
<div class="code-element"><div class="lang-line"><text>shell</text><button class="copy-button" id="code478b" onclick="copyCode(code478, code478b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code478"><div class="highlight"><pre><span></span>&gt;python<span class="w"> </span>-h
usage:<span class="w"> </span>python<span class="w"> </span><span class="o">[</span>option<span class="o">]</span><span class="w"> </span>...<span class="w"> </span><span class="o">[</span>-c<span class="w"> </span>cmd<span class="w"> </span><span class="p">|</span><span class="w"> </span>-m<span class="w"> </span>mod<span class="w"> </span><span class="p">|</span><span class="w"> </span>file<span class="w"> </span><span class="p">|</span><span class="w"> </span>-<span class="o">]</span><span class="w"> </span><span class="o">[</span>arg<span class="o">]</span><span class="w"> </span>...
Options<span class="w"> </span><span class="o">(</span>and<span class="w"> </span>corresponding<span class="w"> </span>environment<span class="w"> </span>variables<span class="o">)</span>:
-b<span class="w">     </span>:<span class="w"> </span>issue<span class="w"> </span>warnings<span class="w"> </span>about<span class="w"> </span>str<span class="o">(</span>bytes_instance<span class="o">)</span>,<span class="w"> </span>str<span class="o">(</span>bytearray_instance<span class="o">)</span>
<span class="w">         </span>and<span class="w"> </span>comparing<span class="w"> </span>bytes/bytearray<span class="w"> </span>with<span class="w"> </span>str.<span class="w"> </span><span class="o">(</span>-bb:<span class="w"> </span>issue<span class="w"> </span>errors<span class="o">)</span>
-B<span class="w">     </span>:<span class="w"> </span><span class="k">do</span><span class="w"> </span>not<span class="w"> </span>write<span class="w"> </span>.pyc<span class="w"> </span>files<span class="w"> </span>on<span class="w"> </span>import<span class="p">;</span><span class="w"> </span>also<span class="w"> </span><span class="nv">PYTHONDONTWRITEBYTECODE</span><span class="o">=</span>x
-c<span class="w"> </span>cmd<span class="w"> </span>:<span class="w"> </span>program<span class="w"> </span>passed<span class="w"> </span><span class="k">in</span><span class="w"> </span>as<span class="w"> </span>string<span class="w"> </span><span class="o">(</span>terminates<span class="w"> </span>option<span class="w"> </span>list<span class="o">)</span>
-d<span class="w">     </span>:<span class="w"> </span>turn<span class="w"> </span>on<span class="w"> </span>parser<span class="w"> </span>debugging<span class="w"> </span>output<span class="w"> </span><span class="o">(</span><span class="k">for</span><span class="w"> </span>experts<span class="w"> </span>only,<span class="w"> </span>only<span class="w"> </span>works<span class="w"> </span>on
<span class="w">         </span>debug<span class="w"> </span>builds<span class="o">)</span><span class="p">;</span><span class="w"> </span>also<span class="w"> </span><span class="nv">PYTHONDEBUG</span><span class="o">=</span>x
-E<span class="w">     </span>:<span class="w"> </span>ignore<span class="w"> </span>PYTHON*<span class="w"> </span>environment<span class="w"> </span>variables<span class="w"> </span><span class="o">(</span>such<span class="w"> </span>as<span class="w"> </span>PYTHONPATH<span class="o">)</span>
-h<span class="w">     </span>:<span class="w"> </span>print<span class="w"> </span>this<span class="w"> </span><span class="nb">help</span><span class="w"> </span>message<span class="w"> </span>and<span class="w"> </span><span class="nb">exit</span><span class="w"> </span><span class="o">(</span>also<span class="w"> </span>-?<span class="w"> </span>or<span class="w"> </span>--help<span class="o">)</span>
-i<span class="w">     </span>:<span class="w"> </span>inspect<span class="w"> </span>interactively<span class="w"> </span>after<span class="w"> </span>running<span class="w"> </span>script<span class="p">;</span><span class="w"> </span>forces<span class="w"> </span>a<span class="w"> </span>prompt<span class="w"> </span>even
<span class="w">         </span><span class="k">if</span><span class="w"> </span>stdin<span class="w"> </span>does<span class="w"> </span>not<span class="w"> </span>appear<span class="w"> </span>to<span class="w"> </span>be<span class="w"> </span>a<span class="w"> </span>terminal<span class="p">;</span><span class="w"> </span>also<span class="w"> </span><span class="nv">PYTHONINSPECT</span><span class="o">=</span>x
-I<span class="w">     </span>:<span class="w"> </span>isolate<span class="w"> </span>Python<span class="w"> </span>from<span class="w"> </span>the<span class="w"> </span>users<span class="w"> </span>environment<span class="w"> </span><span class="o">(</span>implies<span class="w"> </span>-E<span class="w"> </span>and<span class="w"> </span>-s<span class="o">)</span>
-m<span class="w"> </span>mod<span class="w"> </span>:<span class="w"> </span>run<span class="w"> </span>library<span class="w"> </span>module<span class="w"> </span>as<span class="w"> </span>a<span class="w"> </span>script<span class="w"> </span><span class="o">(</span>terminates<span class="w"> </span>option<span class="w"> </span>list<span class="o">)</span>
-O<span class="w">     </span>:<span class="w"> </span>remove<span class="w"> </span>assert<span class="w"> </span>and<span class="w"> </span>__debug__-dependent<span class="w"> </span>statements<span class="p">;</span><span class="w"> </span>add<span class="w"> </span>.opt-1<span class="w"> </span>before
<span class="w">         </span>.pyc<span class="w"> </span>extension<span class="p">;</span><span class="w"> </span>also<span class="w"> </span><span class="nv">PYTHONOPTIMIZE</span><span class="o">=</span>x
-OO<span class="w">    </span>:<span class="w"> </span><span class="k">do</span><span class="w"> </span>-O<span class="w"> </span>changes<span class="w"> </span>and<span class="w"> </span>also<span class="w"> </span>discard<span class="w"> </span>docstrings<span class="p">;</span><span class="w"> </span>add<span class="w"> </span>.opt-2<span class="w"> </span>before
<span class="w">         </span>.pyc<span class="w"> </span>extension
-P<span class="w">     </span>:<span class="w"> </span><span class="k">do</span><span class="w"> </span>not<span class="w"> </span>prepend<span class="w"> </span>a<span class="w"> </span>potentially<span class="w"> </span>unsafe<span class="w"> </span>path<span class="w"> </span>to<span class="w"> </span>sys.path<span class="p">;</span><span class="w"> </span>also<span class="w"> </span>PYTHONSAFEPATH
-q<span class="w">     </span>:<span class="w"> </span><span class="k">do</span><span class="w"> </span>not<span class="w"> </span>print<span class="w"> </span>version<span class="w"> </span>and<span class="w"> </span>copyright<span class="w"> </span>messages<span class="w"> </span>on<span class="w"> </span>interactive<span class="w"> </span>startup
-s<span class="w">     </span>:<span class="w"> </span><span class="k">do</span><span class="w"> </span>not<span class="w"> </span>add<span class="w"> </span>user<span class="w"> </span>site<span class="w"> </span>directory<span class="w"> </span>to<span class="w"> </span>sys.path<span class="p">;</span><span class="w"> </span>also<span class="w"> </span>PYTHONNOUSERSITE
-S<span class="w">     </span>:<span class="w"> </span><span class="k">do</span><span class="w"> </span>not<span class="w"> </span>imply<span class="w"> </span><span class="s1">&#39;import site&#39;</span><span class="w"> </span>on<span class="w"> </span>initialization
-u<span class="w">     </span>:<span class="w"> </span>force<span class="w"> </span>the<span class="w"> </span>stdout<span class="w"> </span>and<span class="w"> </span>stderr<span class="w"> </span>streams<span class="w"> </span>to<span class="w"> </span>be<span class="w"> </span>unbuffered<span class="p">;</span>
<span class="w">         </span>this<span class="w"> </span>option<span class="w"> </span>has<span class="w"> </span>no<span class="w"> </span>effect<span class="w"> </span>on<span class="w"> </span>stdin<span class="p">;</span><span class="w"> </span>also<span class="w"> </span><span class="nv">PYTHONUNBUFFERED</span><span class="o">=</span>x
-v<span class="w">     </span>:<span class="w"> </span>verbose<span class="w"> </span><span class="o">(</span>trace<span class="w"> </span>import<span class="w"> </span>statements<span class="o">)</span><span class="p">;</span><span class="w"> </span>also<span class="w"> </span><span class="nv">PYTHONVERBOSE</span><span class="o">=</span>x
<span class="w">         </span>can<span class="w"> </span>be<span class="w"> </span>supplied<span class="w"> </span>multiple<span class="w"> </span><span class="nb">times</span><span class="w"> </span>to<span class="w"> </span>increase<span class="w"> </span>verbosity
-V<span class="w">     </span>:<span class="w"> </span>print<span class="w"> </span>the<span class="w"> </span>Python<span class="w"> </span>version<span class="w"> </span>number<span class="w"> </span>and<span class="w"> </span><span class="nb">exit</span><span class="w"> </span><span class="o">(</span>also<span class="w"> </span>--version<span class="o">)</span>
<span class="w">         </span>when<span class="w"> </span>given<span class="w"> </span>twice,<span class="w"> </span>print<span class="w"> </span>more<span class="w"> </span>information<span class="w"> </span>about<span class="w"> </span>the<span class="w"> </span>build
-W<span class="w"> </span>arg<span class="w"> </span>:<span class="w"> </span>warning<span class="w"> </span>control<span class="p">;</span><span class="w"> </span>arg<span class="w"> </span>is<span class="w"> </span>action:message:category:module:lineno
<span class="w">         </span>also<span class="w"> </span><span class="nv">PYTHONWARNINGS</span><span class="o">=</span>arg
-x<span class="w">     </span>:<span class="w"> </span>skip<span class="w"> </span>first<span class="w"> </span>line<span class="w"> </span>of<span class="w"> </span>source,<span class="w"> </span>allowing<span class="w"> </span>use<span class="w"> </span>of<span class="w"> </span>non-Unix<span class="w"> </span>forms<span class="w"> </span>of<span class="w"> </span><span class="c1">#!cmd</span>
-X<span class="w"> </span>opt<span class="w"> </span>:<span class="w"> </span><span class="nb">set</span><span class="w"> </span>implementation-specific<span class="w"> </span>option
--check-hash-based-pycs<span class="w"> </span>always<span class="p">|</span>default<span class="p">|</span>never:
<span class="w">         </span>control<span class="w"> </span>how<span class="w"> </span>Python<span class="w"> </span>invalidates<span class="w"> </span>hash-based<span class="w"> </span>.pyc<span class="w"> </span>files
--help-env<span class="w">      </span>:<span class="w"> </span>print<span class="w"> </span><span class="nb">help</span><span class="w"> </span>about<span class="w"> </span>Python<span class="w"> </span>environment<span class="w"> </span>variables<span class="w"> </span>and<span class="w"> </span><span class="nb">exit</span>
--help-xoptions<span class="w"> </span>:<span class="w"> </span>print<span class="w"> </span><span class="nb">help</span><span class="w"> </span>about<span class="w"> </span>implementation-specific<span class="w"> </span>-X<span class="w"> </span>options<span class="w"> </span>and<span class="w"> </span><span class="nb">exit</span>
--help-all<span class="w">      </span>:<span class="w"> </span>print<span class="w"> </span><span class="nb">complete</span><span class="w"> </span><span class="nb">help</span><span class="w"> </span>information<span class="w"> </span>and<span class="w"> </span><span class="nb">exit</span>
Arguments:
file<span class="w">   </span>:<span class="w"> </span>program<span class="w"> </span><span class="nb">read</span><span class="w"> </span>from<span class="w"> </span>script<span class="w"> </span>file
-<span class="w">      </span>:<span class="w"> </span>program<span class="w"> </span><span class="nb">read</span><span class="w"> </span>from<span class="w"> </span>stdin<span class="w"> </span><span class="o">(</span>default<span class="p">;</span><span class="w"> </span>interactive<span class="w"> </span>mode<span class="w"> </span><span class="k">if</span><span class="w"> </span>a<span class="w"> </span>tty<span class="o">)</span>
arg<span class="w"> </span>...:<span class="w"> </span>arguments<span class="w"> </span>passed<span class="w"> </span>to<span class="w"> </span>program<span class="w"> </span><span class="k">in</span><span class="w"> </span>sys.argv<span class="o">[</span><span class="m">1</span>:<span class="o">]</span>
</pre></div></div></div>