| Флаг                  | Описание                                                                                                      |
|-----------------------|---------------------------------------------------------------------------------------------------------------|
| `-r` `--requirements` | Установить пакеты из указанного файла зависимостей `requirements.txt`.                                        |
| `-U` `--upgrade`      | Обновить уже установленные пакеты до последней версии.                                                        |
| `-e` `--editable`     | Установить пакет в режиме редактирования, что позволяет вносить изменения в код и сразу же видеть результаты. |
| `-t` `--target`       | Указать путь к каталогу, в который будут установлены пакеты.                                                  |
| `-f` `--find-links`   | Указать дополнительные источники для поиска пакетов (например, `URL` или путь к локальному каталогу).         |
| `-i` `--index-url`    | Указать `URL` для поиска пакетов в репозитории `PyPI`.                                                        |
| `--no-index`          | Не использовать `PyPI` для поиска пакетов, только локальные источники.                                        |
| `--no-cache-dir`      | Не использовать кэш при установке пакетов.                                                                    |
| `--user`              | Установить пакеты в домашний каталог текущего пользователя.                                                   |


```bash
pip install --help
```

<details>
<summary>uninstall</summary>

```
Usage:
  pip install [options] <requirement specifier> [package-index-options] ...
  pip install [options] -r <requirements file> [package-index-options] ...
  pip install [options] [-e] <vcs project url> ...
  pip install [options] [-e] <local project path> ...
  pip install [options] <archive url/path> ...

Description:
  Install packages from:

  - PyPI (and other indexes) using requirement specifiers.
  - VCS project urls.
  - Local project directories.
  - Local or remote source archives.

  pip also supports installing from "requirements files", which provide
  an easy way to specify a whole environment to be installed.

Install Options:
  -r, --requirement <file>    Install from the given requirements file. This option can be used multiple times.
  -c, --constraint <file>     Constrain versions using the given constraints file. This option can be used multiple times.
  --no-deps                   Don't install package dependencies.
  --pre                       Include pre-release and development versions. By default, pip only finds stable versions.
  -e, --editable <path/url>   Install a project in editable mode (i.e. setuptools "develop mode") from a local project path or a VCS url.
  --dry-run                   Don't actually install anything, just print what would be. Can be used in combination with --ignore-installed to 'resolve'
                              the requirements.
  -t, --target <dir>          Install packages into <dir>. By default this will not replace existing files/folders in <dir>. Use --upgrade to replace
                              existing packages in <dir> with new versions.
  --platform <platform>       Only use wheels compatible with <platform>. Defaults to the platform of the running system. Use this option multiple times
                              to specify multiple platforms supported by the target interpreter.
  --python-version <python_version>
                              The Python interpreter version to use for wheel and "Requires-Python" compatibility checks. Defaults to a version derived
                              from the running interpreter. The version can be specified using up to three dot-separated integers (e.g. "3" for 3.0.0,
                              "3.7" for 3.7.0, or "3.7.3"). A major-minor version can also be given as a string without dots (e.g. "37" for 3.7.0).
  --implementation <implementation>
                              Only use wheels compatible with Python implementation <implementation>, e.g. 'pp', 'jy', 'cp',  or 'ip'. If not specified,
                              then the current interpreter implementation is used.  Use 'py' to force implementation-agnostic wheels.
  --abi <abi>                 Only use wheels compatible with Python abi <abi>, e.g. 'pypy_41'. If not specified, then the current interpreter abi tag is
                              used. Use this option multiple times to specify multiple abis supported by the target interpreter. Generally you will need
                              to specify --implementation, --platform, and --python-version when using this option.
  --user                      Install to the Python user install directory for your platform. Typically ~/.local/, or %APPDATA%/Python on Windows. (See
                              the Python documentation for site.USER_BASE for full details.)
  --root <dir>                Install everything relative to this alternate root directory.
  --prefix <dir>              Installation prefix where lib, bin and other top-level folders are placed. Note that the resulting installation may contain
                              scripts and other resources which reference the Python interpreter of pip, and not that of ``--prefix``. See also the
                              ``--python`` option if the intention is to install packages into another (possibly pip-free) environment.
  --src <dir>                 Directory to check out editable projects into. The default in a virtualenv is "<venv path>/src". The default for global
                              installs is "<current dir>/src".
  -U, --upgrade               Upgrade all specified packages to the newest available version. The handling of dependencies depends on the upgrade-strategy
                              used.
  --upgrade-strategy <upgrade_strategy>
                              Determines how dependency upgrading should be handled [default: only-if-needed]. "eager" - dependencies are upgraded
                              regardless of whether the currently installed version satisfies the requirements of the upgraded package(s). "only-if-
                              needed" -  are upgraded only when they do not satisfy the requirements of the upgraded package(s).
  --force-reinstall           Reinstall all packages even if they are already up-to-date.
  -I, --ignore-installed      Ignore the installed packages, overwriting them. This can break your system if the existing package is of a different
                              version or was installed with a different package manager!
  --ignore-requires-python    Ignore the Requires-Python information.
  --no-build-isolation        Disable isolation when building a modern source distribution. Build dependencies specified by PEP 518 must be already
                              installed if this option is used.
  --use-pep517                Use PEP 517 for building source distributions (use --no-use-pep517 to force legacy behaviour).
  --check-build-dependencies  Check the build dependencies when PEP517 is used.
  --break-system-packages     Allow pip to modify an EXTERNALLY-MANAGED Python installation
  -C, --config-settings <settings>
                              Configuration settings to be passed to the PEP 517 build backend. Settings take the form KEY=VALUE. Use multiple --config-
                              settings options to pass multiple keys to the backend.
  --global-option <options>   Extra global options to be supplied to the setup.py call before the install or bdist_wheel command.
  --compile                   Compile Python source files to bytecode
  --no-compile                Do not compile Python source files to bytecode
  --no-warn-script-location   Do not warn when installing scripts outside PATH
  --no-warn-conflicts         Do not warn about broken dependencies
  --no-binary <format_control>
                              Do not use binary packages. Can be supplied multiple times, and each time adds to the existing value. Accepts either ":all:"
                              to disable all binary packages, ":none:" to empty the set (notice the colons), or one or more package names with commas
                              between them (no colons). Note that some packages are tricky to compile and may fail to install when this option is used on
                              them.
  --only-binary <format_control>
                              Do not use source packages. Can be supplied multiple times, and each time adds to the existing value. Accepts either ":all:"
                              to disable all source packages, ":none:" to empty the set, or one or more package names with commas between them. Packages
                              without binary distributions will fail to install when this option is used on them.
  --prefer-binary             Prefer binary packages over source packages, even if the source packages are newer.
  --require-hashes            Require a hash to check each requirement against, for repeatable installs. This option is implied when any package in a
                              requirements file has a --hash option.
  --progress-bar <progress_bar>
                              Specify whether the progress bar should be used [on, off, raw] (default: on)
  --root-user-action <root_user_action>
                              Action if pip is run as a root user [warn, ignore] (default: warn)
  --report <file>             Generate a JSON file describing what pip did to install the provided requirements. Can be used in combination with --dry-run
                              and --ignore-installed to 'resolve' the requirements. When - is used as file name it writes to stdout. When writing to
                              stdout, please combine with the --quiet option to avoid mixing pip logging output with JSON output.
  --no-clean                  Don't clean up build directories.

Package Index Options:
  -i, --index-url <url>       Base URL of the Python Package Index (default https://pypi.org/simple). This should point to a repository compliant with PEP
                              503 (the simple repository API) or a local directory laid out in the same format.
  --extra-index-url <url>     Extra URLs of package indexes to use in addition to --index-url. Should follow the same rules as --index-url.
  --no-index                  Ignore package index (only looking at --find-links URLs instead).
  -f, --find-links <url>      If a URL or path to an html file, then parse for links to archives such as sdist (.tar.gz) or wheel (.whl) files. If a local
                              path or file:// URL that's a directory, then look for archives in the directory listing. Links to VCS project URLs are not
                              supported.

General Options:
  -h, --help                  Show help.
  --debug                     Let unhandled exceptions propagate outside the main subroutine, instead of logging them to stderr.
  --isolated                  Run pip in an isolated mode, ignoring environment variables and user configuration.
  --require-virtualenv        Allow pip to only run in a virtual environment; exit with an error otherwise.
  --python <python>           Run pip with the specified Python interpreter.
  -v, --verbose               Give more output. Option is additive, and can be used up to 3 times.
  -V, --version               Show version and exit.
  -q, --quiet                 Give less output. Option is additive, and can be used up to 3 times (corresponding to WARNING, ERROR, and CRITICAL logging
                              levels).
  --log <path>                Path to a verbose appending log.
  --no-input                  Disable prompting for input.
  --keyring-provider <keyring_provider>
                              Enable the credential lookup via the keyring library if user input is allowed. Specify which mechanism to use [disabled,
                              import, subprocess]. (default: disabled)
  --proxy <proxy>             Specify a proxy in the form scheme://[user:passwd@]proxy.server:port.
  --retries <retries>         Maximum number of retries each connection should attempt (default 5 times).
  --timeout <sec>             Set the socket timeout (default 15 seconds).
  --exists-action <action>    Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup, (a)bort.
  --trusted-host <hostname>   Mark this host or host:port pair as trusted, even though it does not have valid or any HTTPS.
  --cert <path>               Path to PEM-encoded CA certificate bundle. If provided, overrides the default. See 'SSL Certificate Verification' in pip
                              documentation for more information.
  --client-cert <path>        Path to SSL client certificate, a single file containing the private key and the certificate in PEM format.
  --cache-dir <dir>           Store the cache data in <dir>.
  --no-cache-dir              Disable the cache.
  --disable-pip-version-check
                              Don't periodically check PyPI to determine whether a new version of pip is available for download. Implied with --no-index.
  --no-color                  Suppress colored output.
  --no-python-version-warning
                              Silence deprecation warnings for upcoming unsupported Pythons.
  --use-feature <feature>     Enable new functionality, that may be backward incompatible.
  --use-deprecated <feature>  Enable deprecated functionality, that will be removed in the future.
```
</details>

```bash
pip uninstall --help
```

<details>
<summary>uninstall</summary>

```
Usage:
  pip uninstall [options] <package> ...
  pip uninstall [options] -r <requirements file> ...

Description:
  Uninstall packages.

  pip is able to uninstall most installed packages. Known exceptions are:

  - Pure distutils packages installed with ``python setup.py install``, which
    leave behind no metadata to determine what files were installed.
  - Script wrappers installed by ``python setup.py develop``.

Uninstall Options:
  -r, --requirement <file>    Uninstall all the packages listed in the given requirements file.  This option can be used multiple times.
  -y, --yes                   Don't ask for confirmation of uninstall deletions.
  --root-user-action <root_user_action>
                              Action if pip is run as a root user [warn, ignore] (default: warn)
  --break-system-packages     Allow pip to modify an EXTERNALLY-MANAGED Python installation

General Options:
  -h, --help                  Show help.
  --debug                     Let unhandled exceptions propagate outside the main subroutine, instead of logging them to stderr.
  --isolated                  Run pip in an isolated mode, ignoring environment variables and user configuration.
  --require-virtualenv        Allow pip to only run in a virtual environment; exit with an error otherwise.
  --python <python>           Run pip with the specified Python interpreter.
  -v, --verbose               Give more output. Option is additive, and can be used up to 3 times.
  -V, --version               Show version and exit.
  -q, --quiet                 Give less output. Option is additive, and can be used up to 3 times (corresponding to WARNING, ERROR, and CRITICAL logging
                              levels).
  --log <path>                Path to a verbose appending log.
  --no-input                  Disable prompting for input.
  --keyring-provider <keyring_provider>
                              Enable the credential lookup via the keyring library if user input is allowed. Specify which mechanism to use [auto,
                              disabled, import, subprocess]. (default: auto)
  --proxy <proxy>             Specify a proxy in the form scheme://[user:passwd@]proxy.server:port.
  --retries <retries>         Maximum number of retries each connection should attempt (default 5 times).
  --timeout <sec>             Set the socket timeout (default 15 seconds).
  --exists-action <action>    Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup, (a)bort.
  --trusted-host <hostname>   Mark this host or host:port pair as trusted, even though it does not have valid or any HTTPS.
  --cert <path>               Path to PEM-encoded CA certificate bundle. If provided, overrides the default. See 'SSL Certificate Verification' in pip
                              documentation for more information.
  --client-cert <path>        Path to SSL client certificate, a single file containing the private key and the certificate in PEM format.
  --cache-dir <dir>           Store the cache data in <dir>.
  --no-cache-dir              Disable the cache.
  --disable-pip-version-check
                              Don't periodically check PyPI to determine whether a new version of pip is available for download. Implied with --no-index.
  --no-color                  Suppress colored output.
  --no-python-version-warning
                              Silence deprecation warnings for upcoming unsupported Pythons.
  --use-feature <feature>     Enable new functionality, that may be backward incompatible.
  --use-deprecated <feature>  Enable deprecated functionality, that will be removed in the future.
```
</details>


```bash
pip install <package>           # Установка библиотеки
pip install -U <package>        # Обновление
pip uninstall <package> -y      # Удаление

pip freeze                      # Список зависимостей
pip freeze > requirements.txt   # Сохраняем в файл
pip install -r requirements.txt # Установка из файла

pip list                        # Список установленных библиотек
pip show <package>              # Инфо о библиотеке
pip check                       # Поиск конфликтов версий
pip cache purge                 # Очистка кэша pip
```
