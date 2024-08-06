<table>
<thead>
<tr>
<th>Шаблон</th>
<th>Примеры соответствия</th>
<th>Пояснение</th>
</tr>
</thead>
<tbody>
<tr>
<td>**/logs</td>
<td><code>logs/debug.log</code><br><code>logs/monday/foo.bar</code><br><code>build/logs/debug.log</code></td>
<td>Добавьте в начало шаблона две звездочки,<br>чтобы сопоставлять каталоги в любом месте репозитория.</td>
</tr>
<tr>
<td>**/logs/debug.log</td>
<td><code>logs/debug.log</code><br><code>build/logs/debug.log</code><br>но не<br><code>logs/build/debug.log</code></td>
<td>Две звездочки можно также использовать для сопоставления файлов<br>на основе их имени и имени родительского каталога.</td>
</tr>
<tr>
<td>*.log</td>
<td><code>debug.log</code><br><code>foo.log</code><br>.log<br><code>logs/debug.log</code></td>
<td>Одна звездочка — это подстановочный знак, который может<br>соответствовать как нескольким символам, так и ни одному.</td>
</tr>
<tr>
<td>*.log<br>!important.log</td>
<td><code>debug.log</code><br><code>trace.log</code><br>но не<br><code>important.log</code><br><code>logs/important.log</code></td>
<td>Добавление восклицательного знака в начало шаблона отменяет действие шаблона.<br>Если файл соответствует некоему шаблону,<br>но при этом также соответствует отменяющему шаблону, указанному после,<br>такой файл не будет игнорироваться.</td>
</tr>
<tr>
<td><em>.log<br>!important/</em>.log<br>trace.*</td>
<td><code>debug.log</code><br><code>important/trace.log</code><br>но не<br><code>important/debug.log</code></td>
<td>Шаблоны, указанные после отменяющего шаблона,<br>снова будут помечать файлы как игнорируемые,<br>даже если ранее игнорирование этих файлов было отменено.</td>
</tr>
<tr>
<td>/debug.log</td>
<td><code>debug.log</code><br>но не<br><code>logs/debug.log</code></td>
<td>Косая черта перед именем файла соответствует файлу в корневом каталоге репозитория.</td>
</tr>
<tr>
<td>debug.log</td>
<td><code>debug.log</code><br><code>logs/debug.log</code></td>
<td>По умолчанию шаблоны соответствуют файлам, находящимся в любом каталоге</td>
</tr>
<tr>
<td>debug?.log</td>
<td><code>debug0.log</code><br><code>debugg.log</code><br>но не<br><code>debug10.log</code></td>
<td>Знак вопроса соответствует строго одному символу.</td>
</tr>
<tr>
<td>debug[0-9].log</td>
<td><code>debug0.log</code><br><code>debug1.log</code><br>но не<br><code>debug10.log</code></td>
<td>Квадратные скобки можно также использовать<br>для указания соответствия одному символу из заданного диапазона.</td>
</tr>
<tr>
<td>debug[01].log</td>
<td><code>debug0.log</code><br><code>debug1.log</code><br>но не<br><code>debug2.log</code><br><code>debug01.log</code></td>
<td>Квадратные скобки соответствуют одному символу из указанного набора.</td>
</tr>
<tr>
<td>debug[!01].log</td>
<td><code>debug2.log</code><br>но не<br><code>debug0.log</code><br><code>debug1.log</code><br><code>debug01.log</code></td>
<td>Восклицательный знак можно использовать для указания<br>соответствия любому символу, кроме символов из указанного набора.</td>
</tr>
<tr>
<td>debug[a-z].log</td>
<td><code>debuga.log</code><br><code>debugb.log</code><br>но не<br><code>debug1.log</code></td>
<td>Диапазоны могут быть цифровыми или буквенными.</td>
</tr>
<tr>
<td>logs</td>
<td><code>logs</code><br><code>logs/debug.log</code><br><code>logs/latest/foo.bar</code><br><code>build/logs</code><br><code>build/logs/debug.log</code></td>
<td>Без косой черты в конце этот шаблон будет соответствовать и файлам,<br>и содержимому каталогов с таким именем.<br>В примере соответствия слева игнорируются и каталоги, и файлы с именем <code>logs</code></td>
</tr>
<tr>
<td>logs/</td>
<td><code>logs/debug.log</code><br><code>logs/latest/foo.bar</code><br><code>build/logs/foo.bar</code><br><code>build/logs/latest/debug.log</code></td>
<td>Косая черта в конце шаблона означает каталог.<br>Все содержимое любого каталога репозитория, соответствующего этому имени<br>(включая все его файлы и подкаталоги), будет игнорироваться</td>
</tr>
<tr>
<td>logs/<br>!logs/important.log</td>
<td><code>logs/debug.log</code><br><code>logs/important.log</code></td>
<td>Минуточку!<br>Разве файл <code>logs/important.log</code> из примера слева<br>не должен быть исключен нз списка игнорируемых?<br>Нет!<br>Из-за странностей Git, связанных с производительностью,<br>вы не можете отменить игнорирование файла, которое задано шаблоном соответствия каталогу</td>
</tr>
<tr>
<td>logs/**/debug.log</td>
<td><code>logs/debug.log</code><br><code>logs/monday/debug.log</code><br><code>logs/monday/pm/debug.log</code></td>
<td>Две звездочки соответствуют множеству каталогов или ни одному.</td>
</tr>
<tr>
<td>logs/*day/debug.log</td>
<td><code>logs/monday/debug.log</code><br><code>logs/tuesday/debug.log</code><br>но не<br><code>logs/latest/debug.log</code></td>
<td>Подстановочные символы можно использовать и в именах каталогов.</td>
</tr>
<tr>
<td>logs/debug.log</td>
<td><code>logs/debug.log</code><br>но не<br><code>debug.log</code><br><code>build/logs/debug.log</code></td>
<td>Шаблоны, указывающие на файл в определенном каталоге,<br>задаются относительно корневого каталога репозитория.<br>(При желании можно добавить в начало косую черту, но она ни на что особо не повлияет.)</td>
</tr>
</tbody>
</table>