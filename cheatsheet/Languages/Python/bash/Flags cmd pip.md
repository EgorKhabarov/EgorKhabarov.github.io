<table>
<thead>
<tr>
<th>Флаг</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>-r</code> <code>--requirements</code></td>
<td>Установить пакеты из указанного файла зависимостей <code>requirements.txt</code>.</td>
</tr>
<tr>
<td><code>-U</code> <code>--upgrade</code></td>
<td>Обновить уже установленные пакеты до последней версии.</td>
</tr>
<tr>
<td><code>-e</code> <code>--editable</code></td>
<td>Установить пакет в режиме редактирования, что позволяет вносить изменения в код и сразу же видеть результаты.</td>
</tr>
<tr>
<td><code>-t</code> <code>--target</code></td>
<td>Указать путь к каталогу, в который будут установлены пакеты.</td>
</tr>
<tr>
<td><code>-f</code> <code>--find-links</code></td>
<td>Указать дополнительные источники для поиска пакетов (например, <code>URL</code> или путь к локальному каталогу).</td>
</tr>
<tr>
<td><code>-i</code> <code>--index-url</code></td>
<td>Указать <code>URL</code> для поиска пакетов в репозитории <code>PyPI</code>.</td>
</tr>
<tr>
<td><code>--no-index</code></td>
<td>Не использовать <code>PyPI</code> для поиска пакетов, только локальные источники.</td>
</tr>
<tr>
<td><code>--no-cache-dir</code></td>
<td>Не использовать кэш при установке пакетов.</td>
</tr>
<tr>
<td><code>--user</code></td>
<td>Установить пакеты в домашний каталог текущего пользователя.</td>
</tr>
</tbody>
</table>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span>pip<span class="w"> </span>install<span class="w"> </span>--help
</pre></div></div></div>

<div class="code_element"><div class="lang_line"><text>text</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-text"><div class="highlight"><pre><span></span>Usage:
  pip install [options] &lt;requirement specifier&gt; [package-index-options] ...
  pip install [options] -r &lt;requirements file&gt; [package-index-options] ...
  pip install [options] [-e] &lt;vcs project url&gt; ...
  pip install [options] [-e] &lt;local project path&gt; ...
  pip install [options] &lt;archive url/path&gt; ...

Description:
  Install packages from:

  - PyPI (and other indexes) using requirement specifiers.
  - VCS project urls.
  - Local project directories.
  - Local or remote source archives.

  pip also supports installing from &quot;requirements files&quot;, which provide
  an easy way to specify a whole environment to be installed.

Install Options:
  -r, --requirement &lt;file&gt;    Install from the given requirements file. This option can be used multiple times.
  -c, --constraint &lt;file&gt;     Constrain versions using the given constraints file. This option can be used multiple times.
  --no-deps                   Don&#39;t install package dependencies.
  --pre                       Include pre-release and development versions. By default, pip only finds stable versions.
  -e, --editable &lt;path/url&gt;   Install a project in editable mode (i.e. setuptools &quot;develop mode&quot;) from a local project path or a VCS url.
  --dry-run                   Don&#39;t actually install anything, just print what would be. Can be used in combination with --ignore-installed to &#39;resolve&#39;
                              the requirements.
  -t, --target &lt;dir&gt;          Install packages into &lt;dir&gt;. By default this will not replace existing files/folders in &lt;dir&gt;. Use --upgrade to replace
                              existing packages in &lt;dir&gt; with new versions.
  --platform &lt;platform&gt;       Only use wheels compatible with &lt;platform&gt;. Defaults to the platform of the running system. Use this option multiple times
                              to specify multiple platforms supported by the target interpreter.
  --python-version &lt;python_version&gt;
                              The Python interpreter version to use for wheel and &quot;Requires-Python&quot; compatibility checks. Defaults to a version derived
                              from the running interpreter. The version can be specified using up to three dot-separated integers (e.g. &quot;3&quot; for 3.0.0,
                              &quot;3.7&quot; for 3.7.0, or &quot;3.7.3&quot;). A major-minor version can also be given as a string without dots (e.g. &quot;37&quot; for 3.7.0).
  --implementation &lt;implementation&gt;
                              Only use wheels compatible with Python implementation &lt;implementation&gt;, e.g. &#39;pp&#39;, &#39;jy&#39;, &#39;cp&#39;,  or &#39;ip&#39;. If not specified,
                              then the current interpreter implementation is used.  Use &#39;py&#39; to force implementation-agnostic wheels.
  --abi &lt;abi&gt;                 Only use wheels compatible with Python abi &lt;abi&gt;, e.g. &#39;pypy_41&#39;. If not specified, then the current interpreter abi tag is
                              used. Use this option multiple times to specify multiple abis supported by the target interpreter. Generally you will need
                              to specify --implementation, --platform, and --python-version when using this option.
  --user                      Install to the Python user install directory for your platform. Typically ~/.local/, or %APPDATA%\Python on Windows. (See
                              the Python documentation for site.USER_BASE for full details.)
  --root &lt;dir&gt;                Install everything relative to this alternate root directory.
  --prefix &lt;dir&gt;              Installation prefix where lib, bin and other top-level folders are placed. Note that the resulting installation may contain
                              scripts and other resources which reference the Python interpreter of pip, and not that of ``--prefix``. See also the
                              ``--python`` option if the intention is to install packages into another (possibly pip-free) environment.
  --src &lt;dir&gt;                 Directory to check out editable projects into. The default in a virtualenv is &quot;&lt;venv path&gt;/src&quot;. The default for global
                              installs is &quot;&lt;current dir&gt;/src&quot;.
  -U, --upgrade               Upgrade all specified packages to the newest available version. The handling of dependencies depends on the upgrade-strategy
                              used.
  --upgrade-strategy &lt;upgrade_strategy&gt;
                              Determines how dependency upgrading should be handled [default: only-if-needed]. &quot;eager&quot; - dependencies are upgraded
                              regardless of whether the currently installed version satisfies the requirements of the upgraded package(s). &quot;only-if-
                              needed&quot; -  are upgraded only when they do not satisfy the requirements of the upgraded package(s).
  --force-reinstall           Reinstall all packages even if they are already up-to-date.
  -I, --ignore-installed      Ignore the installed packages, overwriting them. This can break your system if the existing package is of a different
                              version or was installed with a different package manager!
  --ignore-requires-python    Ignore the Requires-Python information.
  --no-build-isolation        Disable isolation when building a modern source distribution. Build dependencies specified by PEP 518 must be already
                              installed if this option is used.
  --use-pep517                Use PEP 517 for building source distributions (use --no-use-pep517 to force legacy behaviour).
  --check-build-dependencies  Check the build dependencies when PEP517 is used.
  --break-system-packages     Allow pip to modify an EXTERNALLY-MANAGED Python installation
  -C, --config-settings &lt;settings&gt;
                              Configuration settings to be passed to the PEP 517 build backend. Settings take the form KEY=VALUE. Use multiple --config-
                              settings options to pass multiple keys to the backend.
  --global-option &lt;options&gt;   Extra global options to be supplied to the setup.py call before the install or bdist_wheel command.
  --compile                   Compile Python source files to bytecode
  --no-compile                Do not compile Python source files to bytecode
  --no-warn-script-location   Do not warn when installing scripts outside PATH
  --no-warn-conflicts         Do not warn about broken dependencies
  --no-binary &lt;format_control&gt;
                              Do not use binary packages. Can be supplied multiple times, and each time adds to the existing value. Accepts either &quot;:all:&quot;
                              to disable all binary packages, &quot;:none:&quot; to empty the set (notice the colons), or one or more package names with commas
                              between them (no colons). Note that some packages are tricky to compile and may fail to install when this option is used on
                              them.
  --only-binary &lt;format_control&gt;
                              Do not use source packages. Can be supplied multiple times, and each time adds to the existing value. Accepts either &quot;:all:&quot;
                              to disable all source packages, &quot;:none:&quot; to empty the set, or one or more package names with commas between them. Packages
                              without binary distributions will fail to install when this option is used on them.
  --prefer-binary             Prefer binary packages over source packages, even if the source packages are newer.
  --require-hashes            Require a hash to check each requirement against, for repeatable installs. This option is implied when any package in a
                              requirements file has a --hash option.
  --progress-bar &lt;progress_bar&gt;
                              Specify whether the progress bar should be used [on, off, raw] (default: on)
  --root-user-action &lt;root_user_action&gt;
                              Action if pip is run as a root user [warn, ignore] (default: warn)
  --report &lt;file&gt;             Generate a JSON file describing what pip did to install the provided requirements. Can be used in combination with --dry-run
                              and --ignore-installed to &#39;resolve&#39; the requirements. When - is used as file name it writes to stdout. When writing to
                              stdout, please combine with the --quiet option to avoid mixing pip logging output with JSON output.
  --no-clean                  Don&#39;t clean up build directories.

Package Index Options:
  -i, --index-url &lt;url&gt;       Base URL of the Python Package Index (default https://pypi.org/simple). This should point to a repository compliant with PEP
                              503 (the simple repository API) or a local directory laid out in the same format.
  --extra-index-url &lt;url&gt;     Extra URLs of package indexes to use in addition to --index-url. Should follow the same rules as --index-url.
  --no-index                  Ignore package index (only looking at --find-links URLs instead).
  -f, --find-links &lt;url&gt;      If a URL or path to an html file, then parse for links to archives such as sdist (.tar.gz) or wheel (.whl) files. If a local
                              path or file:// URL that&#39;s a directory, then look for archives in the directory listing. Links to VCS project URLs are not
                              supported.

General Options:
  -h, --help                  Show help.
  --debug                     Let unhandled exceptions propagate outside the main subroutine, instead of logging them to stderr.
  --isolated                  Run pip in an isolated mode, ignoring environment variables and user configuration.
  --require-virtualenv        Allow pip to only run in a virtual environment; exit with an error otherwise.
  --python &lt;python&gt;           Run pip with the specified Python interpreter.
  -v, --verbose               Give more output. Option is additive, and can be used up to 3 times.
  -V, --version               Show version and exit.
  -q, --quiet                 Give less output. Option is additive, and can be used up to 3 times (corresponding to WARNING, ERROR, and CRITICAL logging
                              levels).
  --log &lt;path&gt;                Path to a verbose appending log.
  --no-input                  Disable prompting for input.
  --keyring-provider &lt;keyring_provider&gt;
                              Enable the credential lookup via the keyring library if user input is allowed. Specify which mechanism to use [disabled,
                              import, subprocess]. (default: disabled)
  --proxy &lt;proxy&gt;             Specify a proxy in the form scheme://[user:passwd@]proxy.server:port.
  --retries &lt;retries&gt;         Maximum number of retries each connection should attempt (default 5 times).
  --timeout &lt;sec&gt;             Set the socket timeout (default 15 seconds).
  --exists-action &lt;action&gt;    Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup, (a)bort.
  --trusted-host &lt;hostname&gt;   Mark this host or host:port pair as trusted, even though it does not have valid or any HTTPS.
  --cert &lt;path&gt;               Path to PEM-encoded CA certificate bundle. If provided, overrides the default. See &#39;SSL Certificate Verification&#39; in pip
                              documentation for more information.
  --client-cert &lt;path&gt;        Path to SSL client certificate, a single file containing the private key and the certificate in PEM format.
  --cache-dir &lt;dir&gt;           Store the cache data in &lt;dir&gt;.
  --no-cache-dir              Disable the cache.
  --disable-pip-version-check
                              Don&#39;t periodically check PyPI to determine whether a new version of pip is available for download. Implied with --no-index.
  --no-color                  Suppress colored output.
  --no-python-version-warning
                              Silence deprecation warnings for upcoming unsupported Pythons.
  --use-feature &lt;feature&gt;     Enable new functionality, that may be backward incompatible.
  --use-deprecated &lt;feature&gt;  Enable deprecated functionality, that will be removed in the future.
</pre></div></div></div>