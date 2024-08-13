<p>Библиотека "mailbox" в Python используется для работы с почтовыми ящиками.
Она позволяет читать и записывать электронные письма в различных форматах, таких как mbox, MMDF, babyl и др.</p>
<p>Таблица методов библиотеки "mailbox":</p>
<table>
<thead>
<tr>
<th>Метод</th>
<th>Краткое описание</th>
</tr>
</thead>
<tbody>
<tr>
<td>mailbox.mbox</td>
<td>Позволяет работать с форматом mbox.</td>
</tr>
<tr>
<td>mailbox.Maildir</td>
<td>Предоставляет доступ к Maildir-формату почтового ящика.</td>
</tr>
<tr>
<td>mailbox.Babyl</td>
<td>Обеспечивает работу с форматом babyl.</td>
</tr>
<tr>
<td>mailbox.MMDF</td>
<td>Позволяет чтение и запись писем в формате MMDF.</td>
</tr>
<tr>
<td>mailbox.Mailbox</td>
<td>Предоставляет общий интерфейс для работы с почтовыми ящиками в разных форматах.</td>
</tr>
<tr>
<td>mailbox.MaildirMessage</td>
<td>Представляет отдельное письмо в формате Maildir.</td>
</tr>
<tr>
<td>mailbox.MH</td>
<td>Работа с письмами в формате MH.</td>
</tr>
</tbody>
</table>
<p>Самые часто используемые методы библиотеки "mailbox":</p>
<p><code>add</code> - добавляет письмо в почтовый ящик.</p>
<pre><code class="language-python">with mailbox.mbox(&quot;sample.mbox&quot;) as mbox:
    message = EmailMessage()
    message[&quot;Subject&quot;] = &quot;Hello&quot;
    message.set_content(&quot;This is a test email&quot;)
    mbox.add(message)
</code></pre>
<p><code>iterkeys</code> - возвращает итератор для ключей (идентификаторов) писем в почтовом ящике.</p>
<pre><code class="language-python">with mailbox.mbox(&quot;sample.mbox&quot;) as mbox:
    for key in mbox.iterkeys():
        print(key)
</code></pre>
<p><code>get_message</code> - возвращает письмо по ключу (идентификатору).</p>
<pre><code class="language-python">with mailbox.mbox(&quot;sample.mbox&quot;) as mbox:
    message = mbox.get_message(&quot;12345&quot;)
    print(message[&quot;Subject&quot;])
</code></pre>
<p><code>remove</code> - удаляет письмо по ключу (идентификатору).</p>
<pre><code class="language-python">with mailbox.mbox(&quot;sample.mbox&quot;) as mbox:
    mbox.remove(&quot;12345&quot;)
</code></pre>