<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>echo "# название" &gt;&gt; README.md</code></td>
<td>Создание файла <code>README.md</code></td>
</tr>
<tr>
<td><code>git init</code></td>
<td>Инициализация репозитория</td>
</tr>
<tr>
<td><code>git add README.md</code></td>
<td>Добавления файла <code>README.md</code> в проект</td>
</tr>
<tr>
<td><code>git commit -m "first commit"</code></td>
<td>Получает проиндексированный снимок состояния<br>и выполняет его коммит в историю проекта</td>
</tr>
<tr>
<td><code>git remote add origin https://github.com/username/repo.git</code></td>
<td>Команда, которой устанавливается подключение<br>к удаленному серверу и <code>git</code> репозиторию, размещающемуся на нем.</td>
</tr>
<tr>
<td><code>git push -u origin master</code></td>
<td>Кзменения отправляются на удаленный сервер</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>git log --oneline</code></td>
<td>Посмотреть все коммиты</td>
</tr>
<tr>
<td><code>git checkout .</code></td>
<td>Восстановить все</td>
</tr>
<tr>
<td><code>git checkout "код коммита"</code></td>
<td>Вернуть до состояния этого коммита</td>
</tr>
<tr>
<td><code>git checkout master</code></td>
<td>Вернуться в ветку мастер</td>
</tr>
</tbody>
</table>
<p>Восстановить файлы на локальном компьютере:
<code>git fetch --all</code></p>
<p><code>git reset --hard origin/master</code> или <code>git reset --hard origin/&lt;название_ветки&gt;</code></p>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>git add text.txt</code></td>
<td>Добавить файл в репозиторий</td>
</tr>
<tr>
<td><code>git rm text.txt</code></td>
<td>Удалить файл</td>
</tr>
<tr>
<td><code>git status</code></td>
<td>Текущее состояние репозитория (изменения, неразрешенные конфликты и тп)</td>
</tr>
<tr>
<td><code>git commit -a -m "Commit description"</code></td>
<td>Сделать коммит</td>
</tr>
<tr>
<td><code>git push origin</code></td>
<td>Замерджить все ветки локального репозитория на удаленный репозиторий</td>
</tr>
<tr>
<td><code>git push origin master</code></td>
<td>Аналогично предыдущему, но делается пуш только ветки master</td>
</tr>
<tr>
<td><code>git push origin HEAD</code></td>
<td>Запушить текущую ветку, не вводя целиком ее название</td>
</tr>
<tr>
<td><code>git pull origin</code></td>
<td>Замерджить все ветки с удаленного репозитория</td>
</tr>
<tr>
<td><code>git pull origin master</code></td>
<td>Аналогично предыдущему, но накатывается только ветка master</td>
</tr>
<tr>
<td><code>git pull origin HEAD</code></td>
<td>Накатить текущую ветку, не вводя ее длинное имя</td>
</tr>
<tr>
<td><code>git fetch origin</code></td>
<td>Скачать все ветки с origin, но не мерджить их в локальный репозиторий</td>
</tr>
<tr>
<td><code>git fetch origin master</code></td>
<td>Аналогично предыдущему, но только для одной заданной ветки</td>
</tr>
<tr>
<td><code>git checkout -b some_branch origin/some_branch</code></td>
<td>Начать работать с веткой some_branch (уже существующей)</td>
</tr>
<tr>
<td><code>git branch some_branch</code></td>
<td>Создать новый бранч (ответвится от текущего)</td>
</tr>
<tr>
<td><code>git checkout some_branch</code></td>
<td>Переключиться на другую ветку (из тех, с которыми уже работаем)</td>
</tr>
<tr>
<td><code>git branch</code></td>
<td>Получаем список веток, с которыми работаем (звездочкой отмечена текущая ветвь)</td>
</tr>
<tr>
<td><code>git branch -a # | grep something</code></td>
<td>Просмотреть все существующие ветви</td>
</tr>
<tr>
<td><code>git merge some_branch</code></td>
<td>Замерджить some_branch в текущую ветку</td>
</tr>
<tr>
<td><code>git branch -d some_branch</code></td>
<td>Удалить бранч (после мерджа)</td>
</tr>
<tr>
<td><code>git branch -D some_branch</code></td>
<td>Просто удалить бранч (тупиковая ветвь)</td>
</tr>
<tr>
<td><code>git show commit_hash</code></td>
<td>Изменения, сделанные в заданном коммите</td>
</tr>
<tr>
<td><code>git push origin :branch-name</code></td>
<td>Удалить бранч из репозитория на сервере</td>
</tr>
<tr>
<td><code>git reset --hard commit_hash</code></td>
<td>Откатиться к конкретному коммиту и удалить последующие (хэш смотрим в «git log»)</td>
</tr>
<tr>
<td><code>git push -f</code></td>
<td>Залить на сервер измененные коммиты</td>
</tr>
<tr>
<td><code>git clean -f</code></td>
<td>Удаление untracked files</td>
</tr>
</tbody>
</table>