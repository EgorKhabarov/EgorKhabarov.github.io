<pre><code class="language-python">chr_digit = [&quot;0&quot;, &quot;1&quot;, &quot;2&quot;, &quot;3&quot;, &quot;4&quot;, &quot;5&quot;, &quot;6&quot;, &quot;7&quot;, &quot;8&quot;, &quot;9&quot;]


def number_to_string(number):
    if number == 0:
        return &quot;0&quot;
    sign = &quot;-&quot; if number &lt; 0 else &quot;&quot;
    number = abs(number)
    digits = []
    while number &gt; 0:
        digit = number % 10
        digits.append(chr_digit[digit])
        number //= 10
    digits.reverse()
    return sign + &quot;&quot;.join(digits)


def string_to_number(string):
    if string == &quot;0&quot;:
        return 0
    sign = 1
    if string[0] == &quot;-&quot;:
        sign = -1
        string = string[1:]
    number = 0
    for char in string:
        digit = chr_digit.index(char)
        number = number * 10 + digit
    return sign * number
</code></pre>
<pre><code class="language-pycon">&gt;&gt;&gt; print(number_to_string(12345))
&quot;12345&quot;
&gt;&gt;&gt; print(string_to_number(&quot;12345&quot;))
12345
</code></pre>