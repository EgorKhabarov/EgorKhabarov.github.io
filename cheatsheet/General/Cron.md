<h1>Format</h1>
<div class="code_element"><div class="lang_line"><text>text</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-text"><div class="highlight"><pre><span></span>Min  Hour Day  Mon  Weekday
*    *    *    *    *  command to be executed
┬    ┬    ┬    ┬    ┬
│    │    │    │    └─  Weekday  (0=Sun .. 6=Sat)
│    │    │    └──────  Month    (1..12)
│    │    └───────────  Day      (1..31)
│    └────────────────  Hour     (0..23)
└─────────────────────  Minute   (0..59)
</pre></div></div></div>

<h1>Operators</h1>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>*</code></td>
<td>All values</td>
</tr>
<tr>
<td><code>,</code></td>
<td>Separate individual values</td>
</tr>
<tr>
<td><code>-</code></td>
<td>A range of values</td>
</tr>
<tr>
<td><code>/</code></td>
<td>Divide a value into steps</td>
</tr>
</tbody>
</table>
<h1>Crontab</h1>
<div class="code_element"><div class="lang_line"><text>text</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-text"><div class="highlight"><pre><span></span># Adding tasks easily
echo &quot;@reboot echo hi&quot; | crontab

# Open in editor - optional for another user
crontab -e [-u user]

# List tasks - optional for another user
crontab -l [-u user]

# Delete crontab file - optional for another user
crontab -r [-u user]
</pre></div></div></div>

<h1>Special strings</h1>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>@reboot</code></td>
<td>Every rebot</td>
</tr>
<tr>
<td><code>@hourly</code></td>
<td>Once every hour - same as <code>0 * * * *</code></td>
</tr>
<tr>
<td><code>@daily</code></td>
<td>Once every day - same as <code>0 0 * * *</code></td>
</tr>
<tr>
<td><code>@midnight</code></td>
<td>Once every midnight - same as <code>@daily</code></td>
</tr>
<tr>
<td><code>@weekly</code></td>
<td>Once every week - same as <code>0 0 * * 0</code></td>
</tr>
<tr>
<td><code>@monthly</code></td>
<td>Once every month - same as <code>0 0 1 * *</code></td>
</tr>
<tr>
<td><code>@yearly</code></td>
<td>Once every year - same as <code>0 0 1 1 *</code></td>
</tr>
</tbody>
</table>
<h1>Examples</h1>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>0 * * * *</code></td>
<td>Every hour</td>
</tr>
<tr>
<td><code>*/15 * * * *</code></td>
<td>Every 15 mins</td>
</tr>
<tr>
<td><code>0 */2 * * *</code></td>
<td>Every 2 hours</td>
</tr>
<tr>
<td><code>0 18 * * 0-6</code></td>
<td>Every week Mon-Sat at 6pm</td>
</tr>
<tr>
<td><code>10 2 * * 6,7</code></td>
<td>Every Sat and Sun on 2:10am</td>
</tr>
<tr>
<td><code>0 0 * * 0</code></td>
<td>Every Sunday midnight</td>
</tr>
</tbody>
</table>