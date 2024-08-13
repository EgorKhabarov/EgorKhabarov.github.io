<p>Библиотека "pyparsing" используется для анализа и разбора текстовых данных в языке программирования Python.
Она предоставляет возможность создавать грамматики и правила для разбора сложных структур данных.</p>
<p>Методы модуля "pyparsing" и его подмодулей:</p>
<p>parseString(string) - Разбирает строку в соответствии с определенной грамматикой и возвращает структурированные данные.
Word(alphas) - Определяет грамматическое правило для разбора последовательности символов, состоящей только из букв.
nums - Подмодуль, содержащий грамматические правила для разбора числовых значений.
CaselessLiteral(string) - Определяет грамматическое правило для разбора нечувствительных к регистру строк.
QuotedString(quoteChar) - Определяет грамматическое правило для разбора строки, заключенной в кавычки.</p>
<p>Самые часто используемые методы "pyparsing" с их кратким описанием и примером кода:</p>
<p>parseString(string): Разбирает строку в соответствии с грамматикой и возвращает структурированные данные.</p>
<pre><code class="language-python">from pyparsing import Word, alphas, nums

data = &quot;Hello World&quot;
print(Word(alphas).parseString(data))  # [&quot;Hello&quot;]
</code></pre>
<p>Word(alphas): Определяет грамматическое правило для разбора последовательности символов, состоящей только из букв.</p>
<pre><code class="language-python">from pyparsing import Word, alphas

data = &quot;Hello123&quot;
print(Word(alphas).parseString(data))  # [&quot;Hello&quot;]
</code></pre>
<p>QuotedString(quoteChar): Определяет грамматическое правило для разбора строки, заключенной в кавычки.</p>
<pre><code class="language-python">from pyparsing import QuotedString

data = '&quot;Hello World&quot;'
print(QuotedString('&quot;').parseString(data))  # [&quot;Hello World&quot;]
</code></pre>