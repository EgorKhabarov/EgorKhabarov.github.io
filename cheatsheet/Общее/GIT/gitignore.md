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
<td>logs/debug.log<br>logs/monday/foo.bar<br>build/logs/debug.log</td>
<td>Добавьте в начало шаблона две звездочки,<br>чтобы сопоставлять каталоги в любом месте репозитория.</td>
</tr>
<tr>
<td>**/logs/debug.log</td>
<td>logs/debug.log<br>build/logs/debug.log<br>но не<br>logs/build/debug.log</td>
<td>Две звездочки можно также использовать для сопоставления файлов<br>на основе их имени и имени родительского каталога.</td>
</tr>
<tr>
<td>*.log</td>
<td>debug.log<br>foo.log<br>.log<br>logs/debug.log</td>
<td>Одна звездочка — это подстановочный знак, который может<br>соответствовать как нескольким символам, так и ни одному.</td>
</tr>
<tr>
<td>*.log<br>!important.log</td>
<td>debug.log<br>trace.log<br>но не<br>important.log<br>logs/important.log</td>
<td>Добавление восклицательного знака в начало шаблона отменяет действие шаблона.<br>Если файл соответствует некоему шаблону,<br>но при этом также соответствует отменяющему шаблону, указанному после,<br>такой файл не будет игнорироваться.</td>
</tr>
<tr>
<td><em>.log<br>!important/</em>.log<br>trace.*</td>
<td>debug.log<br>important/trace.log<br>но не<br>important/debug.log</td>
<td>Шаблоны, указанные после отменяющего шаблона,<br>снова будут помечать файлы как игнорируемые,<br>даже если ранее игнорирование этих файлов было отменено.</td>
</tr>
<tr>
<td>/debug.log</td>
<td>debug.log<br>но не<br>logs/debug.log</td>
<td>Косая черта перед именем файла соответствует файлу в корневом каталоге репозитория.</td>
</tr>
<tr>
<td>debug.log</td>
<td>debug.log<br>logs/debug.log</td>
<td>По умолчанию шаблоны соответствуют файлам, находящимся в любом каталоге</td>
</tr>
<tr>
<td>debug?.log</td>
<td>debug0.log<br>debugg.log<br>но не<br>debug10.log</td>
<td>Знак вопроса соответствует строго одному символу.</td>
</tr>
<tr>
<td>debug[0-9].log</td>
<td>debug0.log<br>debug1.log<br>но не<br>debug10.log</td>
<td>Квадратные скобки можно также использовать<br>для указания соответствия одному символу из заданного диапазона.</td>
</tr>
<tr>
<td>debug[01].log</td>
<td>debug0.log<br>debug1.log<br>но не<br>debug2.log<br>debug01.log</td>
<td>Квадратные скобки соответствуют одному символу из указанного набора.</td>
</tr>
<tr>
<td>debug[!01].log</td>
<td>debug2.log<br>но не<br>debug0.log<br>debug1.log<br>debug01.log</td>
<td>Восклицательный знак можно использовать для указания<br>соответствия любому символу, кроме символов из указанного набора.</td>
</tr>
<tr>
<td>debug[a-z].log</td>
<td>debuga.log<br>debugb.log<br>но не<br>debug1.log</td>
<td>Диапазоны могут быть цифровыми или буквенными.</td>
</tr>
<tr>
<td>logs</td>
<td>logs<br>logs/debug.log<br>logs/latest/foo.bar<br>build/logs<br>build/logs/debug.log</td>
<td>Без косой черты в конце этот шаблон будет соответствовать и файлам,<br>и содержимому каталогов с таким именем.<br>В примере соответствия слева игнорируются и каталоги, и файлы с именем logs</td>
</tr>
<tr>
<td>logs/</td>
<td>logs/debug.log<br>logs/latest/foo.bar<br>build/logs/foo.bar<br>build/logs/latest/debug.log</td>
<td>Косая черта в конце шаблона означает каталог.<br>Все содержимое любого каталога репозитория, соответствующего этому имени<br>(включая все его файлы и подкаталоги), будет игнорироваться</td>
</tr>
<tr>
<td>logs/<br>!logs/important.log</td>
<td>logs/debug.log<br>logs/important.log</td>
<td>Минуточку!<br>Разве файл logs/important.log из примера слева<br>не должен быть исключен нз списка игнорируемых?<br>Нет!<br>Из-за странностей Git, связанных с производительностью,<br>вы не можете отменить игнорирование файла, которое задано шаблоном соответствия каталогу</td>
</tr>
<tr>
<td>logs/**/debug.log</td>
<td>logs/debug.log<br>logs/monday/debug.log<br>logs/monday/pm/debug.log</td>
<td>Две звездочки соответствуют множеству каталогов или ни одному.</td>
</tr>
<tr>
<td>logs/*day/debug.log</td>
<td>logs/monday/debug.log<br>logs/tuesday/debug.log<br>но не<br>logs/latest/debug.log</td>
<td>Подстановочные символы можно использовать и в именах каталогов.</td>
</tr>
<tr>
<td>logs/debug.log</td>
<td>logs/debug.log<br>но не<br>debug.log<br>build/logs/debug.log</td>
<td>Шаблоны, указывающие на файл в определенном каталоге,<br>задаются относительно корневого каталога репозитория.<br>(При желании можно добавить в начало косую черту, но она ни на что особо не повлияет.)</td>
</tr>
</tbody>
</table>