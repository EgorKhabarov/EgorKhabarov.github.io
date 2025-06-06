Команда, которая создает список всех пакетов и их версий,
установленных в настоящее время в среде Python.

```bash
pip freeze > requirements.txt
```

Файл `requirements.txt` используется для указания зависимостей для проекта Python.
В нем перечислены пакеты и их версии, необходимые для правильной работы проекта.
Это упрощает настройку той же среды на другом компьютере или при развертывании приложения в производственной среде.
Когда вы запустите `pip freeze > requirements.txt`, он создаст новый файл с именем `requirements.txt`
в вашем текущем каталоге и запишет вывод `pip freeze` команды в этот файл,
который будет содержать список всех пакетов и их версий, которые в
настоящее время установлены в вашей среде Python, один пакет за строку.
Позже вы можете использовать

```bash
pip install -r requirements.txt
```

для установки всех пакетов и их версий, перечисленныx в файле,
это гарантирует, что среда такая же, как та, которая
использовалась для создания `requirements.txt` файла.

Рекомендуется включить `requirements.txt` файл в репозиторий вашего проекта,
чтобы другие разработчики или пользователи могли легко
настроить ту же среду и запустить проект с правильными зависимостями.

Для создания файла с библиотеками используемыми только для нужного проекта использовать

```bash
pip freeze --local > requirements.txt
```
