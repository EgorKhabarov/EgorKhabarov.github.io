<p><a href="https://github.com/EgorKhabarov/table2string">https://github.com/EgorKhabarov/table2string</a></p>
<h1>table2string</h1>
<p><a href="https://github.com/EgorKhabarov/table2string/actions/workflows/tests.yml"><img alt="GitHub Actions Workflow Status" src="https://img.shields.io/github/actions/workflow/status/EgorKhabarov/table2string/tests.yml?style=flat&amp;logo=GitHub&amp;label=Tests" /></a> <a href="https://github.com/EgorKhabarov/table2string/actions/workflows/publish.yml"><img alt="Publish Python Package to PyPI" src="https://img.shields.io/github/actions/workflow/status/EgorKhabarov/table2string/publish.yml?style=flat&amp;logo=GitHub&amp;label=Publish%20to%20PyPI" /></a></p>
<p><a href="https://pypi.python.org/pypi/table2string"><img alt="PyPi Package Version" src="https://img.shields.io/pypi/v/table2string.svg?style=flat&amp;logo=pypi" /></a> <a href="https://pypi.python.org/pypi/table2string"><img alt="Supported Python versions" src="https://img.shields.io/pypi/pyversions/table2string.svg?style=flat&amp;logo=pypi" /></a> <a href="https://pypi.python.org/pypi/table2string"><img alt="PyPi status" src="https://img.shields.io/pypi/status/table2string.svg?style=flat&amp;logo=pypi" /></a> <a href="https://pypi.org/project/table2string/"><img alt="PyPi downloads" src="https://img.shields.io/pypi/dm/table2string.svg?style=flat&amp;logo=pypi" /></a></p>
<h2>Convert table to string</h2>
<p>While there are several libraries available for converting tables to strings in Python, none seemed to meet my specific requirements. </p>
<ul>
<li><strong>Line Break Support:</strong> Easily include line breaks within cells for enhanced readability.</li>
<li><strong>Emoji Integration:</strong> Effortlessly incorporate emoji characters into your tables to add visual appeal and context.</li>
</ul>
<hr />
<h1>Install</h1>
<h2>PyPI</h2>
<pre><code class="language-shell">pip install -U table2string
</code></pre>
<h2>GitHub</h2>
<pre><code class="language-shell">pip install -U git+https://github.com/EgorKhabarov/table2string.git@master
</code></pre>
<hr />
<h1>Usage example</h1>
<pre><code class="language-pycon">&gt;&gt;&gt; from table2string import Table
&gt;&gt;&gt; Table([(&quot;1&quot;, &quot;2&quot;, &quot;3&quot;), (&quot;qwe&quot;, &quot;rty\nuio&quot;, &quot;&quot;)], name=&quot;Table Name&quot;).print()
+---------------+
|  Table Name   |
+-----+-----+---+
|   1 |   2 | 3 |
+-----+-----+---+
| qwe | rty |   |
|     | uio |   |
+-----+-----+---+
&gt;&gt;&gt; from io import StringIO
&gt;&gt;&gt; Table.from_csv(StringIO('c1,c2,c3\n1,2,3\nqwe,&quot;rty\nuio&quot;,'), name=&quot;Table Name&quot;).print()
+----------------+
|   Table Name   |
+-----+-----+----+
| c1  | c2  | c3 |
+-----+-----+----+
|   1 |   2 |  3 |
+-----+-----+----+
| qwe | rty |    |
|     | uio |    |
+-----+-----+----+
&gt;&gt;&gt; Table.from_csv(StringIO('c1,c2,c3\n1,2,3\nqwe,&quot;rty\nuio&quot;,'), name=&quot;Table Name&quot;, column_names=False).print()
+---------------+
|  Table Name   |
+-----+-----+---+
|   1 |   2 | 3 |
+-----+-----+---+
| qwe | rty |   |
|     | uio |   |
+-----+-----+---+
&gt;&gt;&gt; import sqlite3
&gt;&gt;&gt; cursor = sqlite3.connect(&quot;:memory:&quot;).cursor().execute(
...     &quot;CREATE TABLE data (c1 TEXT, c2 TEXT, c3 TEXT);&quot;
... ).executemany(
...     &quot;INSERT INTO data (c1, c2, c3) VALUES (?, ?, ?);&quot;,
...     [(&quot;1&quot;, &quot;2&quot;, &quot;3&quot;), (&quot;qwe&quot;, &quot;rty\nuio&quot;, &quot;&quot;)],
... ).execute(
...     &quot;SELECT c1, c2, c3 FROM data;&quot;
... )
&gt;&gt;&gt; Table.from_db_cursor(cursor, name=&quot;Table Name&quot;).print()
+---------------+
|  Table Name   |
+-----+-----+---+
|   1 |   2 | 3 |
+-----+-----+---+
| qwe | rty |   |
|     | uio |   |
+-----+-----+---+
&gt;&gt;&gt; Table.from_db_cursor(
...     cursor.execute(&quot;SELECT c1, c2, c3 FROM data;&quot;),
...     name=&quot;Table Name&quot;,
...     column_names=True,
... ).print()
+----------------+
|   Table Name   |
+-----+-----+----+
| c1  | c2  | c3 |
+-----+-----+----+
|   1 |   2 |  3 |
+-----+-----+----+
| qwe | rty |    |
|     | uio |    |
+-----+-----+----+
&gt;&gt;&gt; from table2string import print_table, stringify_table
&gt;&gt;&gt; print_table([(&quot;1&quot;, &quot;2&quot;, &quot;3&quot;), (&quot;qwe&quot;, &quot;rty\nuio&quot;, &quot;&quot;)], name=&quot;Table Name&quot;)
+---------------+
|  Table Name   |
+-----+-----+---+
|   1 |   2 | 3 |
+-----+-----+---+
| qwe | rty |   |
|     | uio |   |
+-----+-----+---+
&gt;&gt;&gt; print(stringify_table([(&quot;1&quot;, &quot;2&quot;, &quot;3&quot;), (&quot;qwe&quot;, &quot;rty\nuio&quot;, &quot;&quot;)], name=&quot;Table Name&quot;))
+---------------+
|  Table Name   |
+-----+-----+---+
|   1 |   2 | 3 |
+-----+-----+---+
| qwe | rty |   |
|     | uio |   |
+-----+-----+---+

</code></pre>
<h2>Custom width and height settings</h2>
<table>
<thead>
<tr>
<th>Width</th>
<th>Example</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>&lt;width&gt;</code></td>
<td><code>10</code></td>
<td>Setting <code>width</code> (<code>10</code>) for the whole table</td>
</tr>
<tr>
<td><code>(&lt;width&gt;,)</code></td>
<td><code>(10,)</code></td>
<td>Setting <code>width_1</code> (<code>10</code>) for all column</td>
</tr>
<tr>
<td><code>(&lt;width_1&gt;, &lt;width_2&gt;)</code></td>
<td><code>(10, 20)</code></td>
<td>Setting <code>width_1</code> (<code>10</code>) for the first column and <code>width_2</code> (<code>20</code>)<br>for all other columns</td>
</tr>
<tr>
<td><code>(&lt;width_1&gt;, &lt;width_2&gt;, &lt;width_3&gt;)</code></td>
<td><code>(10, 20, 30)</code></td>
<td>Setting <code>width_1</code> (<code>10</code>) for the first column and <code>width_2</code> (<code>20</code>)<br>for the second and <code>width_3</code> (<code>30</code>) for the third column</td>
</tr>
</tbody>
</table>
<details>
<summary>Example</summary>


<pre><code class="language-pycon">&gt;&gt;&gt; # Width of the entire table with borders
&gt;&gt;&gt; print_table([(1,), (2.345,), (&quot;example&quot;,)], max_width=10)
+--------+
|      1 |
+--------+
|  2.345 |
+--------+
| exampl↩|
| e      |
+--------+
&gt;&gt;&gt; # Width of each column individually
&gt;&gt;&gt; print_table([(1,), (2.345,), (&quot;example&quot;,)], max_width=(10,))
+------------+
|          1 |
+------------+
|      2.345 |
+------------+
| example    |
+------------+
&gt;&gt;&gt; print_table([(&quot;123456\n\n789000&quot;, &quot;example&quot;)], max_width=(3, 4), max_height=4)
+-----+------+
| 123↩| exam↩|
| 456 | ple  |
|     |      |
| 789…|      |
+-----+------+
&gt;&gt;&gt; print_table([(&quot;123456789&quot;,)], max_width=(1,), max_height=1)
+---+
| 1…|
+---+
&gt;&gt;&gt; print_table(
...     table=[(&quot;123\n456\n789&quot;,)],
...     max_width=(3,),
...     max_height=4,
...     maximize_height=True,
... )
+-----+
| 123 |
| 456 |
| 789 |
|     |
+-----+
&gt;&gt;&gt; print_table(
...     table=[(&quot;123456789&quot;,)],
...     max_width=(3,),
...     max_height=4,
...     maximize_height=True,
... )
+-----+
| 123↩|
| 456↩|
| 789 |
|     |
+-----+

</code></pre>

</details>

<h2>Text alignment</h2>
<table>
<thead>
<tr>
<th>Align</th>
<th>Example</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>"&lt;align&gt;"</code> or <code>("&lt;align&gt;",)</code></td>
<td><code>"^"</code> or <code>("^",)</code></td>
<td>Setting <code>align</code> (<code>"^"</code>) for all columns</td>
</tr>
<tr>
<td><code>("&lt;align_1&gt;", "&lt;align_2&gt;")</code></td>
<td><code>("^", "&lt;")</code></td>
<td>Setting <code>align_1</code> (<code>"^"</code>) for the first column and <code>align_2</code> (<code>"&lt;"</code>)<br>for all other columns</td>
</tr>
<tr>
<td><code>("&lt;align_1&gt;", "&lt;align_2&gt;", "&lt;align_3&gt;")</code></td>
<td><code>("^", "&lt;", "&gt;")</code></td>
<td>Setting <code>align_1</code> (<code>"^"</code>) for the first column and <code>align_2</code> (<code>"&lt;"</code>)<br>for the second and <code>align_3</code> (<code>"&gt;"</code>) for the third column</td>
</tr>
</tbody>
</table>
<h3>ALLOWED_ALIGNS</h3>
<table>
<thead>
<tr>
<th style="text-align: center;">Align</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><code>*</code> or <code>**</code></td>
<td>Alignment depends on the type. If this is a number and there are no line breaks in this cell,<br>then align to the right; otherwise, align to the left.</td>
</tr>
<tr>
<td style="text-align: center;"><code>&lt;</code> or <code>&lt;&lt;</code></td>
<td>All lines are left aligned</td>
</tr>
<tr>
<td style="text-align: center;"><code>^</code> or <code>^^</code></td>
<td>All lines are center aligned</td>
</tr>
<tr>
<td style="text-align: center;"><code>&gt;</code> or <code>&gt;&gt;</code></td>
<td>All lines are right aligned</td>
</tr>
<tr>
<td style="text-align: center;"><code>&lt;^</code></td>
<td>The first line is left aligned and the remaining lines are centered</td>
</tr>
<tr>
<td style="text-align: center;"><code>&lt;&gt;</code></td>
<td>The first line is left aligned and the remaining lines are right aligned</td>
</tr>
<tr>
<td style="text-align: center;"><code>^&lt;</code></td>
<td>The first line is aligned to the center, and the remaining lines are aligned to the left of the first line.</td>
</tr>
<tr>
<td style="text-align: center;"><code>^&gt;</code></td>
<td>The first line is aligned to the center, and the remaining lines are aligned to the right of the first line.</td>
</tr>
<tr>
<td style="text-align: center;"><code>&gt;&lt;</code></td>
<td>The first line is right aligned and the remaining lines are left aligned</td>
</tr>
<tr>
<td style="text-align: center;"><code>&gt;^</code></td>
<td>The first line is right aligned and the remaining lines are centered</td>
</tr>
</tbody>
</table>
<details>
<summary>Example</summary>


<pre><code class="language-pycon">&gt;&gt;&gt; kwargs_1 = {
...     &quot;table&quot;: [(&quot;1&quot;, &quot;123456789\nqwerty\nasdfghjklzxcvb&quot;)],
...     &quot;name&quot;: &quot;Table Name\nName\nNaaaaame&quot;,
...     &quot;column_names&quot;: (&quot;1&quot;, &quot;col 2\nc2&quot;),
...     &quot;max_width&quot;: (5, 15),
... }
&gt;&gt;&gt; print_table(**kwargs_1)
+-------------------------+
|       Table Name        |
|          Name           |
|        Naaaaame         |
+-------+-----------------+
|   1   |      col 2      |
|       |       c2        |
+-------+-----------------+
|     1 | 123456789       |
|       | qwerty          |
|       | asdfghjklzxcvb  |
+-------+-----------------+
&gt;&gt;&gt; print_table(**kwargs_1, align=&quot;*&quot;, name_align=&quot;*&quot;, column_names_align=&quot;*&quot;)  # align=&quot;**&quot;, name_align=&quot;**&quot;, column_names_align=&quot;**&quot;
+-------------------------+
| Table Name              |
| Name                    |
| Naaaaame                |
+-------+-----------------+
|     1 | col 2           |
|       | c2              |
+-------+-----------------+
|     1 | 123456789       |
|       | qwerty          |
|       | asdfghjklzxcvb  |
+-------+-----------------+
&gt;&gt;&gt; print_table(**kwargs_1, align=&quot;&lt;&quot;, name_align=&quot;&lt;&quot;, column_names_align=&quot;&lt;&quot;)  # align=&quot;&lt;&lt;&quot;, name_align=&quot;&lt;&lt;&quot;, column_names_align=&quot;&lt;&lt;&quot;
+-------------------------+
| Table Name              |
| Name                    |
| Naaaaame                |
+-------+-----------------+
| 1     | col 2           |
|       | c2              |
+-------+-----------------+
| 1     | 123456789       |
|       | qwerty          |
|       | asdfghjklzxcvb  |
+-------+-----------------+
&gt;&gt;&gt; print_table(**kwargs_1, align=&quot;&gt;&quot;, name_align=&quot;&gt;&quot;, column_names_align=&quot;&gt;&quot;)  # align=&quot;&gt;&gt;&quot;, name_align=&quot;&gt;&gt;&quot;, column_names_align=&quot;&gt;&gt;&quot;
+-------------------------+
|              Table Name |
|                    Name |
|                Naaaaame |
+-------+-----------------+
|     1 |           col 2 |
|       |              c2 |
+-------+-----------------+
|     1 |       123456789 |
|       |          qwerty |
|       |  asdfghjklzxcvb |
+-------+-----------------+
&gt;&gt;&gt; print_table(**kwargs_1, align=&quot;^&quot;, name_align=&quot;^&quot;, column_names_align=&quot;^&quot;)  # align=&quot;^^&quot;, name_align=&quot;^^&quot;, column_names_align=&quot;^^&quot;
+-------------------------+
|       Table Name        |
|          Name           |
|        Naaaaame         |
+-------+-----------------+
|   1   |      col 2      |
|       |       c2        |
+-------+-----------------+
|   1   |    123456789    |
|       |     qwerty      |
|       | asdfghjklzxcvb  |
+-------+-----------------+
&gt;&gt;&gt; print_table(**kwargs_1, align=&quot;^&lt;&quot;, name_align=&quot;^&lt;&quot;, column_names_align=&quot;^&lt;&quot;)
+-------------------------+
|       Table Name        |
|       Name              |
|       Naaaaame          |
+-------+-----------------+
|   1   |      col 2      |
|       |      c2         |
+-------+-----------------+
|   1   | 123456789       |
|       | qwerty          |
|       | asdfghjklzxcvb  |
+-------+-----------------+
&gt;&gt;&gt; print_table(**kwargs_1, align=&quot;^&gt;&quot;, name_align=&quot;^&gt;&quot;, column_names_align=&quot;^&gt;&quot;)
+-------------------------+
|       Table Name        |
|             Name        |
|         Naaaaame        |
+-------+-----------------+
|   1   |      col 2      |
|       |         c2      |
+-------+-----------------+
|   1   |      123456789  |
|       |         qwerty  |
|       | asdfghjklzxcvb  |
+-------+-----------------+
&gt;&gt;&gt; print_table([(&quot;qwerty\n123456789\nasdfghjklzxcvb&quot;,)], max_width=(18,), align=&quot;^&lt;&quot;)
+--------------------+
|   qwerty           |
|   123456789        |
|   asdfghjklzxcvb   |
+--------------------+
&gt;&gt;&gt; print_table([(&quot;qwerty\n123456789\nasdfghjklzxcvb&quot;,)], max_width=(18,), align=&quot;^&gt;&quot;)
+--------------------+
|           qwerty   |
|        123456789   |
|   asdfghjklzxcvb   |
+--------------------+

</code></pre>

</details>

<h2>Separator settings</h2>
<table>
<thead>
<tr>
<th>Separator</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>sep=True</code></td>
<td>All horizontal dividers included</td>
</tr>
<tr>
<td><code>sep=False</code></td>
<td>All horizontal dividers are disabled</td>
</tr>
<tr>
<td><code>sep=(1,)</code></td>
<td>Only first delimiter</td>
</tr>
<tr>
<td><code>sep=(1, 3, 5)</code></td>
<td>Only first third and fifth separator</td>
</tr>
<tr>
<td><code>sep=range(1, 100, 5)</code></td>
<td>Delimiter every five lines first 100 lines</td>
</tr>
</tbody>
</table>
<details>
<summary>Example</summary>


<pre><code class="language-pycon">&gt;&gt;&gt; table_1 = [(&quot;qwe&quot;, &quot;rty\nuio&quot;), (&quot;123456\n\n789000&quot;, &quot;example&quot;)]
&gt;&gt;&gt; kwargs = {
...     &quot;max_width&quot;: (3, 4),
...     &quot;max_height&quot;: 4,
... }
&gt;&gt;&gt; print_table(table_1, **kwargs, sep=True)
+-----+------+
| qwe | rty  |
|     | uio  |
+-----+------+
| 123↩| exam↩|
| 456 | ple  |
|     |      |
| 789…|      |
+-----+------+
&gt;&gt;&gt; print_table(table_1, **kwargs, sep=False)
+-----+------+
| qwe | rty  |
|     | uio  |
| 123↩| exam↩|
| 456 | ple  |
|     |      |
| 789…|      |
+-----+------+
&gt;&gt;&gt; table_2 = [(&quot;1&quot;, &quot;2&quot;), (&quot;3&quot;, &quot;4&quot;)]
&gt;&gt;&gt; print_table(table_2, sep=True, name=&quot;Name&quot;)
+-------+
| Name  |
+---+---+
| 1 | 2 |
+---+---+
| 3 | 4 |
+---+---+
&gt;&gt;&gt; print_table(table_2, sep=False, name=&quot;Name&quot;)
+-------+
| Name  |
+---+---+
| 1 | 2 |
| 3 | 4 |
+---+---+
&gt;&gt;&gt; table_3 = [(&quot;1&quot;, &quot;2&quot;), (&quot;3&quot;, &quot;4&quot;), (&quot;5&quot;, &quot;6&quot;), (&quot;7&quot;, &quot;8&quot;)]
&gt;&gt;&gt; print_table(table_3, sep=(1,))
+---+---+
| 1 | 2 |
+---+---+
| 3 | 4 |
| 5 | 6 |
| 7 | 8 |
+---+---+
&gt;&gt;&gt; print_table(table_3, sep=(2,))
+---+---+
| 1 | 2 |
| 3 | 4 |
+---+---+
| 5 | 6 |
| 7 | 8 |
+---+---+
&gt;&gt;&gt; print_table(table_3, sep=(1, 3))
+---+---+
| 1 | 2 |
+---+---+
| 3 | 4 |
| 5 | 6 |
+---+---+
| 7 | 8 |
+---+---+
&gt;&gt;&gt; print_table(table_3, sep=(1,), name=&quot;Name&quot;)
+-------+
| Name  |
+---+---+
| 1 | 2 |
+---+---+
| 3 | 4 |
| 5 | 6 |
| 7 | 8 |
+---+---+
&gt;&gt;&gt; print_table(table_3, sep=(2,), name=&quot;Name&quot;)
+-------+
| Name  |
+---+---+
| 1 | 2 |
| 3 | 4 |
+---+---+
| 5 | 6 |
| 7 | 8 |
+---+---+
&gt;&gt;&gt; print_table(table_3, sep=(1, 3), name=&quot;Name&quot;)
+-------+
| Name  |
+---+---+
| 1 | 2 |
+---+---+
| 3 | 4 |
| 5 | 6 |
+---+---+
| 7 | 8 |
+---+---+

</code></pre>


</details>

<h2>Borders</h2>
<details>
<summary>Border types</summary>


<pre><code class="language-text">┌──────────────┬───────────────────┐
│  ascii_thin  │ ascii_thin_double │
│  +---+---+   │     +---+---+     │
│  |   |   |   │     |   |   |     │
│  +---+---+   │     +===+===+     │
│  |   |   |   │     |   |   |     │
│  +---+---+   │     +---+---+     │
│  |   |   |   │     |   |   |     │
│  +---+---+   │     +---+---+     │
├──────────────┼───────────────────┤
│ ascii_double │ ascii_double_thin │
│  +===+===+   │     +===+===+     │
│  ‖   ‖   ‖   │     ‖   ‖   ‖     │
│  +===+===+   │     +---+---+     │
│  ‖   ‖   ‖   │     ‖   ‖   ‖     │
│  +===+===+   │     +===+===+     │
│  ‖   ‖   ‖   │     ‖   ‖   ‖     │
│  +===+===+   │     +===+===+     │
├──────────────┼───────────────────┤
│     thin     │    thin_thick     │
│  ┌───┬───┐   │     ┌───┬───┐     │
│  │   │   │   │     │   │   │     │
│  ├───┼───┤   │     ┝━━━┿━━━┥     │
│  │   │   │   │     │   │   │     │
│  ├───┼───┤   │     ├───┼───┤     │
│  │   │   │   │     │   │   │     │
│  └───┴───┘   │     └───┴───┘     │
├──────────────┼───────────────────┤
│ thin_double  │  rounded_double   │
│  ┌───┬───┐   │     ╭───┬───╮     │
│  │   │   │   │     │   │   │     │
│  ╞═══╪═══╡   │     ╞═══╪═══╡     │
│  │   │   │   │     │   │   │     │
│  ├───┼───┤   │     ├───┼───┤     │
│  │   │   │   │     │   │   │     │
│  └───┴───┘   │     ╰───┴───╯     │
├──────────────┼───────────────────┤
│   rounded    │   rounded_thick   │
│  ╭───┬───╮   │     ╭───┬───╮     │
│  │   │   │   │     │   │   │     │
│  ├───┼───┤   │     ┝━━━┿━━━┥     │
│  │   │   │   │     │   │   │     │
│  ├───┼───┤   │     ├───┼───┤     │
│  │   │   │   │     │   │   │     │
│  ╰───┴───╯   │     ╰───┴───╯     │
├──────────────┼───────────────────┤
│    thick     │    thick_thin     │
│  ┏━━━┳━━━┓   │     ┌───┬───┐     │
│  ┃   ┃   ┃   │     │   │   │     │
│  ┣━━━╋━━━┫   │     ┠━━━╂━━━┨     │
│  ┃   ┃   ┃   │     │   │   │     │
│  ┣━━━╋━━━┫   │     ├───┼───┤     │
│  ┃   ┃   ┃   │     │   │   │     │
│  ┗━━━┻━━━┛   │     └───┴───┘     │
├──────────────┼───────────────────┤
│    double    │    double_thin    │
│  ╔═══╦═══╗   │     ╔═══╦═══╗     │
│  ║   ║   ║   │     ║   ║   ║     │
│  ╠═══╬═══╣   │     ╟───╫───╢     │
│  ║   ║   ║   │     ║   ║   ║     │
│  ╠═══╬═══╣   │     ╠═══╬═══╣     │
│  ║   ║   ║   │     ║   ║   ║     │
│  ╚═══╩═══╝   │     ╚═══╩═══╝     │
├──────────────┼───────────────────┤
│   booktabs   │  ascii_booktabs   │
│   ───────    │      -------      │
│              │                   │
│   ━━━━━━━    │      =======      │
│              │                   │
│   ───────    │      -------      │
│              │                   │
│   ───────    │      -------      │
├──────────────┼───────────────────┤
│   markdown   │                   │
│  |   |   |   │                   │
│  |---|---|   │                   │
│  |   |   |   │                   │
│  |   |   |   │                   │
└──────────────┴───────────────────┘
</code></pre>


</details>

<details>
<summary>Example</summary>


<pre><code class="language-pycon">&gt;&gt;&gt; from table2string import Table, Themes
&gt;&gt;&gt; name = &quot;Table Name&quot;
&gt;&gt;&gt; column_names = (&quot;c1&quot;, &quot;c2&quot;, &quot;3&quot;)
&gt;&gt;&gt; table = [(&quot;1&quot;, &quot;2&quot;, &quot;3&quot;), (&quot;qwe&quot;, &quot;rty\nuio&quot;, &quot;&quot;)]
&gt;&gt;&gt; t = Table(table)
&gt;&gt;&gt; t_name = Table(table, name=name)
&gt;&gt;&gt; t_column_names = Table(table, column_names=column_names)
&gt;&gt;&gt; t_name_column_names = Table(table, name=name, column_names=column_names)

</code></pre>


<details>
<summary>Themes.ascii_thin</summary>


<pre><code class="language-pycon">
&gt;&gt;&gt; t.print(theme=Themes.ascii_thin)
+-----+-----+---+
|   1 |   2 | 3 |
+-----+-----+---+
| qwe | rty |   |
|     | uio |   |
+-----+-----+---+
&gt;&gt;&gt; t_column_names.print(theme=Themes.ascii_thin)
+-----+-----+---+
| c1  | c2  | 3 |
+-----+-----+---+
|   1 |   2 | 3 |
+-----+-----+---+
| qwe | rty |   |
|     | uio |   |
+-----+-----+---+
&gt;&gt;&gt; t_name.print(theme=Themes.ascii_thin)
+---------------+
|  Table Name   |
+-----+-----+---+
|   1 |   2 | 3 |
+-----+-----+---+
| qwe | rty |   |
|     | uio |   |
+-----+-----+---+
&gt;&gt;&gt; t_name_column_names.print(theme=Themes.ascii_thin)
+---------------+
|  Table Name   |
+-----+-----+---+
| c1  | c2  | 3 |
+-----+-----+---+
|   1 |   2 | 3 |
+-----+-----+---+
| qwe | rty |   |
|     | uio |   |
+-----+-----+---+
</code></pre>


</details>


<details>
<summary>Themes.ascii_thin_double</summary>


<pre><code class="language-pycon">&gt;&gt;&gt; t.print(theme=Themes.ascii_thin_double)
+-----+-----+---+
|   1 |   2 | 3 |
+=====+=====+===+
| qwe | rty |   |
|     | uio |   |
+-----+-----+---+
&gt;&gt;&gt; t_column_names.print(theme=Themes.ascii_thin_double)
+-----+-----+---+
| c1  | c2  | 3 |
+=====+=====+===+
|   1 |   2 | 3 |
+-----+-----+---+
| qwe | rty |   |
|     | uio |   |
+-----+-----+---+
&gt;&gt;&gt; t_name.print(theme=Themes.ascii_thin_double)
+---------------+
|  Table Name   |
+-----+-----+---+
|   1 |   2 | 3 |
+=====+=====+===+
| qwe | rty |   |
|     | uio |   |
+-----+-----+---+
&gt;&gt;&gt; t_name_column_names.print(theme=Themes.ascii_thin_double)
+---------------+
|  Table Name   |
+-----+-----+---+
| c1  | c2  | 3 |
+=====+=====+===+
|   1 |   2 | 3 |
+-----+-----+---+
| qwe | rty |   |
|     | uio |   |
+-----+-----+---+
</code></pre>


</details>


<details>
<summary>Themes.ascii_double</summary>


<pre><code class="language-pycon">&gt;&gt;&gt; t.print(theme=Themes.ascii_double)
+=====+=====+===+
‖   1 ‖   2 ‖ 3 ‖
+=====+=====+===+
‖ qwe ‖ rty ‖   ‖
‖     ‖ uio ‖   ‖
+=====+=====+===+
&gt;&gt;&gt; t_column_names.print(theme=Themes.ascii_double)
+=====+=====+===+
‖ c1  ‖ c2  ‖ 3 ‖
+=====+=====+===+
‖   1 ‖   2 ‖ 3 ‖
+=====+=====+===+
‖ qwe ‖ rty ‖   ‖
‖     ‖ uio ‖   ‖
+=====+=====+===+
&gt;&gt;&gt; t_name.print(theme=Themes.ascii_double)
+===============+
‖  Table Name   ‖
+=====+=====+===+
‖   1 ‖   2 ‖ 3 ‖
+=====+=====+===+
‖ qwe ‖ rty ‖   ‖
‖     ‖ uio ‖   ‖
+=====+=====+===+
&gt;&gt;&gt; t_name_column_names.print(theme=Themes.ascii_double)
+===============+
‖  Table Name   ‖
+=====+=====+===+
‖ c1  ‖ c2  ‖ 3 ‖
+=====+=====+===+
‖   1 ‖   2 ‖ 3 ‖
+=====+=====+===+
‖ qwe ‖ rty ‖   ‖
‖     ‖ uio ‖   ‖
+=====+=====+===+
</code></pre>


</details>


<details>
<summary>Themes.ascii_double_thin</summary>


<pre><code class="language-pycon">&gt;&gt;&gt; t.print(theme=Themes.ascii_double_thin)
+=====+=====+===+
‖   1 ‖   2 ‖ 3 ‖
+-----+-----+---+
‖ qwe ‖ rty ‖   ‖
‖     ‖ uio ‖   ‖
+=====+=====+===+
&gt;&gt;&gt; t_column_names.print(theme=Themes.ascii_double_thin)
+=====+=====+===+
‖ c1  ‖ c2  ‖ 3 ‖
+-----+-----+---+
‖   1 ‖   2 ‖ 3 ‖
+=====+=====+===+
‖ qwe ‖ rty ‖   ‖
‖     ‖ uio ‖   ‖
+=====+=====+===+
&gt;&gt;&gt; t_name.print(theme=Themes.ascii_double_thin)
+===============+
‖  Table Name   ‖
+=====+=====+===+
‖   1 ‖   2 ‖ 3 ‖
+-----+-----+---+
‖ qwe ‖ rty ‖   ‖
‖     ‖ uio ‖   ‖
+=====+=====+===+
&gt;&gt;&gt; t_name_column_names.print(theme=Themes.ascii_double_thin)
+===============+
‖  Table Name   ‖
+=====+=====+===+
‖ c1  ‖ c2  ‖ 3 ‖
+-----+-----+---+
‖   1 ‖   2 ‖ 3 ‖
+=====+=====+===+
‖ qwe ‖ rty ‖   ‖
‖     ‖ uio ‖   ‖
+=====+=====+===+
</code></pre>


</details>


<details>
<summary>Themes.ascii_booktabs</summary>


<pre><code class="language-pycon">&gt;&gt;&gt; t.print(theme=Themes.ascii_booktabs)
 --------------- 
    1     2   3  
 =============== 
  qwe   rty      
        uio      
 --------------- 
&gt;&gt;&gt; t_column_names.print(theme=Themes.ascii_booktabs)
 --------------- 
  c1    c2    3  
 =============== 
    1     2   3  
 --------------- 
  qwe   rty      
        uio      
 --------------- 
&gt;&gt;&gt; t_name.print(theme=Themes.ascii_booktabs)
 --------------- 
   Table Name    
 --------------- 
    1     2   3  
 =============== 
  qwe   rty      
        uio      
 --------------- 
&gt;&gt;&gt; t_name_column_names.print(theme=Themes.ascii_booktabs)
 --------------- 
   Table Name    
 --------------- 
  c1    c2    3  
 =============== 
    1     2   3  
 --------------- 
  qwe   rty      
        uio      
 --------------- 
</code></pre>


</details>


<details>
<summary>Themes.thin</summary>


<pre><code class="language-pycon">&gt;&gt;&gt; t.print(theme=Themes.thin)
┌─────┬─────┬───┐
│   1 │   2 │ 3 │
├─────┼─────┼───┤
│ qwe │ rty │   │
│     │ uio │   │
└─────┴─────┴───┘
&gt;&gt;&gt; t_column_names.print(theme=Themes.thin)
┌─────┬─────┬───┐
│ c1  │ c2  │ 3 │
├─────┼─────┼───┤
│   1 │   2 │ 3 │
├─────┼─────┼───┤
│ qwe │ rty │   │
│     │ uio │   │
└─────┴─────┴───┘
&gt;&gt;&gt; t_name.print(theme=Themes.thin)
┌───────────────┐
│  Table Name   │
├─────┬─────┬───┤
│   1 │   2 │ 3 │
├─────┼─────┼───┤
│ qwe │ rty │   │
│     │ uio │   │
└─────┴─────┴───┘
&gt;&gt;&gt; t_name_column_names.print(theme=Themes.thin)
┌───────────────┐
│  Table Name   │
├─────┬─────┬───┤
│ c1  │ c2  │ 3 │
├─────┼─────┼───┤
│   1 │   2 │ 3 │
├─────┼─────┼───┤
│ qwe │ rty │   │
│     │ uio │   │
└─────┴─────┴───┘
</code></pre>


</details>


<details>
<summary>Themes.thin_thick</summary>


<pre><code class="language-pycon">&gt;&gt;&gt; t.print(theme=Themes.thin_thick)
┌─────┬─────┬───┐
│   1 │   2 │ 3 │
┝━━━━━┿━━━━━┿━━━┥
│ qwe │ rty │   │
│     │ uio │   │
└─────┴─────┴───┘
&gt;&gt;&gt; t_column_names.print(theme=Themes.thin_thick)
┌─────┬─────┬───┐
│ c1  │ c2  │ 3 │
┝━━━━━┿━━━━━┿━━━┥
│   1 │   2 │ 3 │
├─────┼─────┼───┤
│ qwe │ rty │   │
│     │ uio │   │
└─────┴─────┴───┘
&gt;&gt;&gt; t_name.print(theme=Themes.thin_thick)
┌───────────────┐
│  Table Name   │
├─────┬─────┬───┤
│   1 │   2 │ 3 │
┝━━━━━┿━━━━━┿━━━┥
│ qwe │ rty │   │
│     │ uio │   │
└─────┴─────┴───┘
&gt;&gt;&gt; t_name_column_names.print(theme=Themes.thin_thick)
┌───────────────┐
│  Table Name   │
├─────┬─────┬───┤
│ c1  │ c2  │ 3 │
┝━━━━━┿━━━━━┿━━━┥
│   1 │   2 │ 3 │
├─────┼─────┼───┤
│ qwe │ rty │   │
│     │ uio │   │
└─────┴─────┴───┘
</code></pre>


</details>


<details>
<summary>Themes.thin_double</summary>


<pre><code class="language-pycon">&gt;&gt;&gt; t.print(theme=Themes.thin_double)
┌─────┬─────┬───┐
│   1 │   2 │ 3 │
╞═════╪═════╪═══╡
│ qwe │ rty │   │
│     │ uio │   │
└─────┴─────┴───┘
&gt;&gt;&gt; t_column_names.print(theme=Themes.thin_double)
┌─────┬─────┬───┐
│ c1  │ c2  │ 3 │
╞═════╪═════╪═══╡
│   1 │   2 │ 3 │
├─────┼─────┼───┤
│ qwe │ rty │   │
│     │ uio │   │
└─────┴─────┴───┘
&gt;&gt;&gt; t_name.print(theme=Themes.thin_double)
┌───────────────┐
│  Table Name   │
├─────┬─────┬───┤
│   1 │   2 │ 3 │
╞═════╪═════╪═══╡
│ qwe │ rty │   │
│     │ uio │   │
└─────┴─────┴───┘
&gt;&gt;&gt; t_name_column_names.print(theme=Themes.thin_double)
┌───────────────┐
│  Table Name   │
├─────┬─────┬───┤
│ c1  │ c2  │ 3 │
╞═════╪═════╪═══╡
│   1 │   2 │ 3 │
├─────┼─────┼───┤
│ qwe │ rty │   │
│     │ uio │   │
└─────┴─────┴───┘
</code></pre>


</details>


<details>
<summary>Themes.rounded</summary>


<pre><code class="language-pycon">&gt;&gt;&gt; t.print(theme=Themes.rounded)
╭─────┬─────┬───╮
│   1 │   2 │ 3 │
├─────┼─────┼───┤
│ qwe │ rty │   │
│     │ uio │   │
╰─────┴─────┴───╯
&gt;&gt;&gt; t_column_names.print(theme=Themes.rounded)
╭─────┬─────┬───╮
│ c1  │ c2  │ 3 │
├─────┼─────┼───┤
│   1 │   2 │ 3 │
├─────┼─────┼───┤
│ qwe │ rty │   │
│     │ uio │   │
╰─────┴─────┴───╯
&gt;&gt;&gt; t_name.print(theme=Themes.rounded)
╭───────────────╮
│  Table Name   │
├─────┬─────┬───┤
│   1 │   2 │ 3 │
├─────┼─────┼───┤
│ qwe │ rty │   │
│     │ uio │   │
╰─────┴─────┴───╯
&gt;&gt;&gt; t_name_column_names.print(theme=Themes.rounded)
╭───────────────╮
│  Table Name   │
├─────┬─────┬───┤
│ c1  │ c2  │ 3 │
├─────┼─────┼───┤
│   1 │   2 │ 3 │
├─────┼─────┼───┤
│ qwe │ rty │   │
│     │ uio │   │
╰─────┴─────┴───╯
</code></pre>


</details>


<details>
<summary>Themes.rounded_thick</summary>


<pre><code class="language-pycon">&gt;&gt;&gt; t.print(theme=Themes.rounded_thick)
╭─────┬─────┬───╮
│   1 │   2 │ 3 │
┝━━━━━┿━━━━━┿━━━┥
│ qwe │ rty │   │
│     │ uio │   │
╰─────┴─────┴───╯
&gt;&gt;&gt; t_column_names.print(theme=Themes.rounded_thick)
╭─────┬─────┬───╮
│ c1  │ c2  │ 3 │
┝━━━━━┿━━━━━┿━━━┥
│   1 │   2 │ 3 │
├─────┼─────┼───┤
│ qwe │ rty │   │
│     │ uio │   │
╰─────┴─────┴───╯
&gt;&gt;&gt; t_name.print(theme=Themes.rounded_thick)
╭───────────────╮
│  Table Name   │
├─────┬─────┬───┤
│   1 │   2 │ 3 │
┝━━━━━┿━━━━━┿━━━┥
│ qwe │ rty │   │
│     │ uio │   │
╰─────┴─────┴───╯
&gt;&gt;&gt; t_name_column_names.print(theme=Themes.rounded_thick)
╭───────────────╮
│  Table Name   │
├─────┬─────┬───┤
│ c1  │ c2  │ 3 │
┝━━━━━┿━━━━━┿━━━┥
│   1 │   2 │ 3 │
├─────┼─────┼───┤
│ qwe │ rty │   │
│     │ uio │   │
╰─────┴─────┴───╯
</code></pre>


</details>


<details>
<summary>Themes.rounded_double</summary>


<pre><code class="language-pycon">&gt;&gt;&gt; t.print(theme=Themes.rounded_double)
╭─────┬─────┬───╮
│   1 │   2 │ 3 │
╞═════╪═════╪═══╡
│ qwe │ rty │   │
│     │ uio │   │
╰─────┴─────┴───╯
&gt;&gt;&gt; t_column_names.print(theme=Themes.rounded_double)
╭─────┬─────┬───╮
│ c1  │ c2  │ 3 │
╞═════╪═════╪═══╡
│   1 │   2 │ 3 │
├─────┼─────┼───┤
│ qwe │ rty │   │
│     │ uio │   │
╰─────┴─────┴───╯
&gt;&gt;&gt; t_name.print(theme=Themes.rounded_double)
╭───────────────╮
│  Table Name   │
├─────┬─────┬───┤
│   1 │   2 │ 3 │
╞═════╪═════╪═══╡
│ qwe │ rty │   │
│     │ uio │   │
╰─────┴─────┴───╯
&gt;&gt;&gt; t_name_column_names.print(theme=Themes.rounded_double)
╭───────────────╮
│  Table Name   │
├─────┬─────┬───┤
│ c1  │ c2  │ 3 │
╞═════╪═════╪═══╡
│   1 │   2 │ 3 │
├─────┼─────┼───┤
│ qwe │ rty │   │
│     │ uio │   │
╰─────┴─────┴───╯
</code></pre>


</details>


<details>
<summary>Themes.thick</summary>


<pre><code class="language-pycon">&gt;&gt;&gt; t.print(theme=Themes.thick)
┏━━━━━┳━━━━━┳━━━┓
┃   1 ┃   2 ┃ 3 ┃
┣━━━━━╋━━━━━╋━━━┫
┃ qwe ┃ rty ┃   ┃
┃     ┃ uio ┃   ┃
┗━━━━━┻━━━━━┻━━━┛
&gt;&gt;&gt; t_column_names.print(theme=Themes.thick)
┏━━━━━┳━━━━━┳━━━┓
┃ c1  ┃ c2  ┃ 3 ┃
┣━━━━━╋━━━━━╋━━━┫
┃   1 ┃   2 ┃ 3 ┃
┣━━━━━╋━━━━━╋━━━┫
┃ qwe ┃ rty ┃   ┃
┃     ┃ uio ┃   ┃
┗━━━━━┻━━━━━┻━━━┛
&gt;&gt;&gt; t_name.print(theme=Themes.thick)
┏━━━━━━━━━━━━━━━┓
┃  Table Name   ┃
┣━━━━━┳━━━━━┳━━━┫
┃   1 ┃   2 ┃ 3 ┃
┣━━━━━╋━━━━━╋━━━┫
┃ qwe ┃ rty ┃   ┃
┃     ┃ uio ┃   ┃
┗━━━━━┻━━━━━┻━━━┛
&gt;&gt;&gt; t_name_column_names.print(theme=Themes.thick)
┏━━━━━━━━━━━━━━━┓
┃  Table Name   ┃
┣━━━━━┳━━━━━┳━━━┫
┃ c1  ┃ c2  ┃ 3 ┃
┣━━━━━╋━━━━━╋━━━┫
┃   1 ┃   2 ┃ 3 ┃
┣━━━━━╋━━━━━╋━━━┫
┃ qwe ┃ rty ┃   ┃
┃     ┃ uio ┃   ┃
┗━━━━━┻━━━━━┻━━━┛
</code></pre>


</details>


<details>
<summary>Themes.thick_thin</summary>


<pre><code class="language-pycon">&gt;&gt;&gt; t.print(theme=Themes.thick_thin)
┌─────┬─────┬───┐
│   1 │   2 │ 3 │
┠━━━━━╂━━━━━╂━━━┨
│ qwe │ rty │   │
│     │ uio │   │
└─────┴─────┴───┘
&gt;&gt;&gt; t_column_names.print(theme=Themes.thick_thin)
┌─────┬─────┬───┐
│ c1  │ c2  │ 3 │
┠━━━━━╂━━━━━╂━━━┨
│   1 │   2 │ 3 │
├─────┼─────┼───┤
│ qwe │ rty │   │
│     │ uio │   │
└─────┴─────┴───┘
&gt;&gt;&gt; t_name.print(theme=Themes.thick_thin)
┌───────────────┐
│  Table Name   │
├─────┬─────┬───┤
│   1 │   2 │ 3 │
┠━━━━━╂━━━━━╂━━━┨
│ qwe │ rty │   │
│     │ uio │   │
└─────┴─────┴───┘
&gt;&gt;&gt; t_name_column_names.print(theme=Themes.thick_thin)
┌───────────────┐
│  Table Name   │
├─────┬─────┬───┤
│ c1  │ c2  │ 3 │
┠━━━━━╂━━━━━╂━━━┨
│   1 │   2 │ 3 │
├─────┼─────┼───┤
│ qwe │ rty │   │
│     │ uio │   │
└─────┴─────┴───┘
</code></pre>


</details>


<details>
<summary>Themes.double</summary>


<pre><code class="language-pycon">&gt;&gt;&gt; t.print(theme=Themes.double)
╔═════╦═════╦═══╗
║   1 ║   2 ║ 3 ║
╠═════╬═════╬═══╣
║ qwe ║ rty ║   ║
║     ║ uio ║   ║
╚═════╩═════╩═══╝
&gt;&gt;&gt; t_column_names.print(theme=Themes.double)
╔═════╦═════╦═══╗
║ c1  ║ c2  ║ 3 ║
╠═════╬═════╬═══╣
║   1 ║   2 ║ 3 ║
╠═════╬═════╬═══╣
║ qwe ║ rty ║   ║
║     ║ uio ║   ║
╚═════╩═════╩═══╝
&gt;&gt;&gt; t_name.print(theme=Themes.double)
╔═══════════════╗
║  Table Name   ║
╠═════╦═════╦═══╣
║   1 ║   2 ║ 3 ║
╠═════╬═════╬═══╣
║ qwe ║ rty ║   ║
║     ║ uio ║   ║
╚═════╩═════╩═══╝
&gt;&gt;&gt; t_name_column_names.print(theme=Themes.double)
╔═══════════════╗
║  Table Name   ║
╠═════╦═════╦═══╣
║ c1  ║ c2  ║ 3 ║
╠═════╬═════╬═══╣
║   1 ║   2 ║ 3 ║
╠═════╬═════╬═══╣
║ qwe ║ rty ║   ║
║     ║ uio ║   ║
╚═════╩═════╩═══╝
</code></pre>


</details>


<details>
<summary>Themes.double_thin</summary>


<pre><code class="language-pycon">&gt;&gt;&gt; t.print(theme=Themes.double_thin)
╔═════╦═════╦═══╗
║   1 ║   2 ║ 3 ║
╟─────╫─────╫───╢
║ qwe ║ rty ║   ║
║     ║ uio ║   ║
╚═════╩═════╩═══╝
&gt;&gt;&gt; t_column_names.print(theme=Themes.double_thin)
╔═════╦═════╦═══╗
║ c1  ║ c2  ║ 3 ║
╟─────╫─────╫───╢
║   1 ║   2 ║ 3 ║
╠═════╬═════╬═══╣
║ qwe ║ rty ║   ║
║     ║ uio ║   ║
╚═════╩═════╩═══╝
&gt;&gt;&gt; t_name.print(theme=Themes.double_thin)
╔═══════════════╗
║  Table Name   ║
╠═════╦═════╦═══╣
║   1 ║   2 ║ 3 ║
╟─────╫─────╫───╢
║ qwe ║ rty ║   ║
║     ║ uio ║   ║
╚═════╩═════╩═══╝
&gt;&gt;&gt; t_name_column_names.print(theme=Themes.double_thin)
╔═══════════════╗
║  Table Name   ║
╠═════╦═════╦═══╣
║ c1  ║ c2  ║ 3 ║
╟─────╫─────╫───╢
║   1 ║   2 ║ 3 ║
╠═════╬═════╬═══╣
║ qwe ║ rty ║   ║
║     ║ uio ║   ║
╚═════╩═════╩═══╝
</code></pre>


</details>


<details>
<summary>Themes.booktabs</summary>


<pre><code class="language-pycon">&gt;&gt;&gt; t.print(theme=Themes.booktabs)
 ─────────────── 
    1     2   3  
 ━━━━━━━━━━━━━━━ 
  qwe   rty      
        uio      
 ─────────────── 
&gt;&gt;&gt; t_column_names.print(theme=Themes.booktabs)
 ─────────────── 
  c1    c2    3  
 ━━━━━━━━━━━━━━━ 
    1     2   3  
 ─────────────── 
  qwe   rty      
        uio      
 ─────────────── 
&gt;&gt;&gt; t_name.print(theme=Themes.booktabs)
 ─────────────── 
   Table Name    
 ─────────────── 
    1     2   3  
 ━━━━━━━━━━━━━━━ 
  qwe   rty      
        uio      
 ─────────────── 
&gt;&gt;&gt; t_name_column_names.print(theme=Themes.booktabs)
 ─────────────── 
   Table Name    
 ─────────────── 
  c1    c2    3  
 ━━━━━━━━━━━━━━━ 
    1     2   3  
 ─────────────── 
  qwe   rty      
        uio      
 ─────────────── 
</code></pre>


</details>


<details>
<summary>Themes.markdown</summary>


<pre><code class="language-pycon">&gt;&gt;&gt; t.print(theme=Themes.markdown)
|   1 |   2 | 3 |
|-----|-----|---|
| qwe | rty |   |
|     | uio |   |
&gt;&gt;&gt; t_column_names.print(theme=Themes.markdown)
| c1  | c2  | 3 |
|-----|-----|---|
|   1 |   2 | 3 |
| qwe | rty |   |
|     | uio |   |
&gt;&gt;&gt; t_name.print(theme=Themes.markdown)
|  Table Name   |
|   1 |   2 | 3 |
|-----|-----|---|
| qwe | rty |   |
|     | uio |   |
&gt;&gt;&gt; t_name_column_names.print(theme=Themes.markdown)
|  Table Name   |
| c1  | c2  | 3 |
|-----|-----|---|
|   1 |   2 | 3 |
| qwe | rty |   |
|     | uio |   |
</code></pre>


</details>
</details>

<h2>Emojis</h2>
<details>
<summary>Example</summary>


<pre><code class="language-python">from prettytable import PrettyTable
from table2string import Table

names = (&quot;plain text&quot;, &quot;emoji&quot;)
table = [
    (
        &quot;text\ntext&quot;,
        &quot;👨‍👩‍👧‍👦👨‍👩‍👦‍👦👨‍👩‍👧‍👧\n&quot;
        &quot;👨‍👨‍👧‍👦👨‍👨‍👧‍👧👨‍👩‍👧👩‍❤️‍👨\n&quot;
        &quot;👨‍❤️‍👨👯👩‍🦼👭👨‍👩‍👧‍👦\n&quot;
        &quot;👨‍👨‍👧‍👦👨‍👨‍👦👩‍👩‍👧\n&quot;
        &quot;👨‍👨‍👧‍👧👨‍👩‍👦‍👦&quot;,
    ),
]
t = PrettyTable(title=&quot;prettytable&quot;, field_names=names, align=&quot;c&quot;)
t.add_rows(table)
print(t)

t = Table(table, name=&quot;table2string&quot;, column_names=names)
t.print(align=&quot;^&quot;, sep=(1,))
</code></pre>


<details>
    <summary>Windows Terminal</summary>
    <img alt="emoji_example_1.png" src="https://raw.githubusercontent.com/EgorKhabarov/table2string/master/images/emoji_example_Windows_Terminal.png">
</details>

<details>
    <summary>Windows 10</summary>
    <img alt="emoji_example_windows_10_terminal.png" src="https://raw.githubusercontent.com/EgorKhabarov/table2string/master/images/emoji_example_windows_10_terminal.png">
</details>

<details>
    <summary>Windows 11</summary>
    <img alt="emoji_example_windows_11_terminal.png" src="https://raw.githubusercontent.com/EgorKhabarov/table2string/master/images/emoji_example_windows_11_terminal.png">
</details>

<details>
    <summary>VT100 terminal emulator</summary>
    <img alt="emoji_example_VT100_terminal_emulator.png" src="https://raw.githubusercontent.com/EgorKhabarov/table2string/master/images/emoji_example_VT100_terminal_emulator.png">
</details>
</details>