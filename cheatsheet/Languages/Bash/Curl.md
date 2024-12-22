<p><a href="https://devhints.io/curl">https://devhints.io/curl</a></p>
<h1>Options</h1>
<div class="code_element"><div class="lang_line"><text>text</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-text"><div class="highlight"><pre><span></span>-o &lt;file&gt;    # --output: write to file
-u user:pass # --user: Authentication
-v           # --verbose
-vv          # Even more verbose
-s           # --silent: don&#39;t show progress meter or errors
-S           # --show-error: when used with --silent (-sS), show errors but no progress meter
-i           # --include: Include the HTTP-header in the output
-I           # --head: headers only
</pre></div></div></div>

<h1>Request</h1>
<div class="code_element"><div class="lang_line"><text>text</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-text"><div class="highlight"><pre><span></span>-X POST          # --request
-L               # follow link if page redirects
-F               # --form: HTTP POST data for multipart/form-data
</pre></div></div></div>

<h1>Data</h1>
<div class="code_element"><div class="lang_line"><text>text</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-text"><div class="highlight"><pre><span></span>-d &#39;data&#39;    # --data: HTTP post data, URL encoded (eg, status=&quot;Hello&quot;)
-d @file     # --data via file
-G           # --get: send -d data via get
</pre></div></div></div>

<h1>Headers</h1>
<div class="code_element"><div class="lang_line"><text>text</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-text"><div class="highlight"><pre><span></span>-A &lt;str&gt;         # --user-agent
-b name=val      # --cookie
-b FILE          # --cookie
-H &quot;X-Foo: y&quot;    # --header
--compressed     # use deflate/gzip
</pre></div></div></div>

<h1>SSL</h1>
<div class="code_element"><div class="lang_line"><text>text</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-text"><div class="highlight"><pre><span></span>--cacert &lt;file&gt;
    --capath &lt;dir&gt;
-E, --cert &lt;cert&gt;     # --cert: Client cert file
    --cert-type       # der/pem/eng
-k, --insecure        # for self-signed certs
</pre></div></div></div>

<h1>Examples</h1>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span><span class="c1"># Post data:</span>
curl<span class="w"> </span>-d<span class="w"> </span><span class="nv">password</span><span class="o">=</span>x<span class="w"> </span>http://x.com/y
</pre></div></div></div>

<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span><span class="c1"># Auth/data:</span>
curl<span class="w"> </span>-u<span class="w"> </span>user:pass<span class="w"> </span>-d<span class="w"> </span><span class="nv">status</span><span class="o">=</span><span class="s2">&quot;Hello&quot;</span><span class="w"> </span>http://twitter.com/statuses/update.xml
</pre></div></div></div>

<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span><span class="c1"># multipart file upload</span>
curl<span class="w"> </span>-v<span class="w"> </span>--include<span class="w"> </span>--form<span class="w"> </span><span class="nv">key1</span><span class="o">=</span>value1<span class="w"> </span>--form<span class="w"> </span><span class="nv">upload</span><span class="o">=</span>@localfilename<span class="w"> </span>URL
</pre></div></div></div>

<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span><span class="c1"># multipart form: send data from text field and upload file</span>
curl<span class="w"> </span>-F<span class="w"> </span><span class="nv">person</span><span class="o">=</span>anonymous<span class="w"> </span>-F<span class="w"> </span><span class="nv">secret</span><span class="o">=</span>@file.txt<span class="w"> </span>http://example.com/submit.cgi
</pre></div></div></div>

<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span><span class="c1"># Use Curl to Check if a remote resource is available</span>
<span class="c1"># details: https://matthewsetter.com/check-if-file-is-available-with-curl/</span>
curl<span class="w"> </span>-o<span class="w"> </span>/dev/null<span class="w"> </span>--silent<span class="w"> </span>-Iw<span class="w"> </span><span class="s2">&quot;%{http_code}&quot;</span><span class="w"> </span>https://example.com/my.remote.tarball.gz
</pre></div></div></div>