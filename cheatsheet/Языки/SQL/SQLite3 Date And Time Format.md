<p>copied from <a href='https://www.sqlite.org/lang_datefunc.html' target='_blank'>https://www.sqlite.org/lang_datefunc.html</a></p>
<h2>Overview</h2>
<p>SQLite supports seven scalar date and time functions as follows:</p>
<ol>
<li><code>date(time-value, modifier, modifier, ...)</code>  YYYY-MM-DD</li>
<li><code>time(time-value, modifier, modifier, ...)</code>  HH:MM:SS or as HH:MM:SS.SSS</li>
<li><code>datetime(time-value, modifier, modifier, ...)</code>  YYYY-MM-DD HH:MM:SS or as YYYY-MM-DD HH:MM:SS.SSS</li>
<li><code>julianday(time-value, modifier, modifier, ...)</code>  - the fractional number of days since noon in Greenwich on November 24, 4714 B.C.</li>
<li><code>unixepoch(time-value, modifier, modifier, ...)</code>  unix timestamp</li>
<li><code>strftime(format, time-value, modifier, modifier, ...)</code></li>
<li><code>timediff(time-value, time-value)</code></li>
</ol>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>%d</td>
<td>day of month: <code>01-31</code></td>
</tr>
<tr>
<td>%e</td>
<td>day of month without leading zero: <code>1-31</code></td>
</tr>
<tr>
<td>%f</td>
<td>fractional seconds: SS.SSS</td>
</tr>
<tr>
<td>%F</td>
<td>ISO 8601 date: <code>YYYY-MM-DD</code></td>
</tr>
<tr>
<td>%G</td>
<td>ISO 8601 year corresponding to <code>%V</code></td>
</tr>
<tr>
<td>%g</td>
<td>2-digit ISO 8601 year corresponding to <code>%V</code></td>
</tr>
<tr>
<td>%H</td>
<td>hour: <code>00-24</code></td>
</tr>
<tr>
<td>%I</td>
<td>hour for 12-hour clock: <code>01-12</code></td>
</tr>
<tr>
<td>%j</td>
<td>day of year: <code>001-366</code></td>
</tr>
<tr>
<td>%J</td>
<td>Julian day number (fractional)</td>
</tr>
<tr>
<td>%k</td>
<td>hour without leading zero: <code>0-24</code></td>
</tr>
<tr>
<td>%l</td>
<td>%I without leading zero: <code>1-12</code></td>
</tr>
<tr>
<td>%m</td>
<td>month: <code>01-12</code></td>
</tr>
<tr>
<td>%M</td>
<td>minute: <code>00-59</code></td>
</tr>
<tr>
<td>%p</td>
<td>"<code>AM</code>" or "<code>PM</code>" depending on the hour</td>
</tr>
<tr>
<td>%P</td>
<td>"<code>am</code>" or "<code>pm</code>" depending on the hour</td>
</tr>
<tr>
<td>%R</td>
<td>ISO 8601 time: <code>HH:MM</code></td>
</tr>
<tr>
<td>%s</td>
<td>seconds since <code>1970-01-01</code></td>
</tr>
<tr>
<td>%S</td>
<td>seconds: <code>00-59</code></td>
</tr>
<tr>
<td>%T</td>
<td>ISO 8601 time: <code>HH:MM:SS</code></td>
</tr>
<tr>
<td>%U</td>
<td>week of year (<code>00-53</code>) - week 01 starts on the first Sunday</td>
</tr>
<tr>
<td>%u</td>
<td>day of week <code>1-7</code> with Monday==1</td>
</tr>
<tr>
<td>%V</td>
<td>ISO 8601 week of year</td>
</tr>
<tr>
<td>%w</td>
<td>day of week <code>0-6</code> with Sunday==0</td>
</tr>
<tr>
<td>%W</td>
<td>week of year (<code>00-53</code>) - week 01 starts on the first Monday</td>
</tr>
<tr>
<td>%Y</td>
<td>year: <code>0000-9999</code></td>
</tr>
<tr>
<td>%%</td>
<td>%</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th>Function</th>
<th>Equivalent <code>strftime()</code></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>date(...)</code></td>
<td><code>strftime('%F', ...)</code></td>
</tr>
<tr>
<td><code>time(...)</code></td>
<td><code>strftime('%T', ...)</code></td>
</tr>
<tr>
<td><code>datetime(...)</code></td>
<td><code>strftime('%F %T', ...)</code></td>
</tr>
<tr>
<td><code>julianday(...)</code></td>
<td><code>CAST(strftime('%J', ...) as REAL)</code></td>
</tr>
<tr>
<td><code>unixepoch(...)</code></td>
<td><code>CAST(strftime('%s', ...) as INT)</code></td>
</tr>
</tbody>
</table>
<div class="code-element"><div class="lang-line"><text>sql</text><button class="copy-button" id="code6a39c6faa029610b4dd3774cc9b4f509b" onclick="copyCode(code6a39c6faa029610b4dd3774cc9b4f509, code6a39c6faa029610b4dd3774cc9b4f509b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code6a39c6faa029610b4dd3774cc9b4f509"><div class="highlight"><pre><span></span><span class="k">SELECT</span><span class="w"> </span><span class="n">timediff</span><span class="p">(</span><span class="s1">&#39;2023-02-15&#39;</span><span class="p">,</span><span class="s1">&#39;2023-03-15&#39;</span><span class="p">);</span>
</pre></div></div></div>

<h2>Time Values</h2>
<p>A time-value can be in any of the following formats shown below.
The value is usually a string, though it can be an integer or floating point number in the case of format 12.</p>
<ol>
<li><code>YYYY-MM-DD</code></li>
<li><code>YYYY-MM-DD HH:MM</code></li>
<li><code>YYYY-MM-DD HH:MM:SS</code></li>
<li><code>YYYY-MM-DD HH:MM:SS.SSS</code></li>
<li><code>YYYY-MM-DDTHH:MM</code></li>
<li><code>YYYY-MM-DDTHH:MM:SS</code></li>
<li><code>YYYY-MM-DDTHH:MM:SS.SSS</code></li>
<li><code>HH:MM</code></li>
<li><code>HH:MM:SS</code></li>
<li><code>HH:MM:SS.SSS</code></li>
<li><code>now</code></li>
<li><code>DDDDDDDDDD</code></li>
</ol>
<h2>Modifiers</h2>
<p>For all date/time functions other than <code>timediff()</code>, the time-value argument can be followed by zero or more modifiers that alter date and/or time.
Each modifier is a transformation that is applied to the time-value to its left.
Modifiers are applied from left to right; order is important.
The available modifiers are as follows.</p>
<ol>
<li><code>NNN days</code></li>
<li><code>NNN hours</code></li>
<li><code>NNN minutes</code></li>
<li><code>NNN seconds</code></li>
<li><code>NNN months</code></li>
<li><code>NNN years</code></li>
<li><code>±HH:MM</code></li>
<li><code>±HH:MM:SS</code></li>
<li><code>±HH:MM:SS.SSS</code></li>
<li><code>±YYYY-MM-DD</code></li>
<li><code>±YYYY-MM-DD HH:MM</code></li>
<li><code>±YYYY-MM-DD HH:MM:SS</code></li>
<li><code>±YYYY-MM-DD HH:MM:SS.SSS</code></li>
<li><code>ceiling</code></li>
<li><code>floor</code></li>
<li><code>start of month</code></li>
<li><code>start of year</code></li>
<li><code>start of day</code></li>
<li><code>weekday N</code></li>
<li><code>unixepoch</code></li>
<li><code>julianday</code></li>
<li><code>auto</code></li>
<li><code>localtime</code></li>
<li><code>utc</code></li>
<li><code>subsec</code></li>
<li><code>subsecond</code></li>
</ol>