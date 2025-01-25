Библиотека "errno" в Python используется для обработки ошибок, связанных с системными вызовами и функциями операционной системы.
Она предоставляет доступ к кодам ошибок, которые могут возникать
при выполнении операций ввода-вывода, работы с файлами, сетью и другими системными ресурсами.

Методы и подмодули библиотеки "errno":

errno.errorcode: Возвращает словарь, ключами которого являются коды ошибок, а значениями - соответствующие им символьные имена.
errno.geterrno(): Возвращает код текущей ошибки.
errno.geterror(): Возвращает описание текущей ошибки в виде строки.
errno.strerror(errno): Возвращает описание ошибки по заданному коду ошибки.
errno.clear(): Очищает код текущей ошибки.

Самые часто используемые методы библиотеки "errno":

errno.errorcode: Возвращает словарь, где ключами являются коды ошибок, а значениями - символьные имена.
Например: {"ENOENT": "No such file or directory", "EACCES": "Permission denied"}.

```python
import errno

error_codes = errno.errorcode
print(error_codes)
```

errno.geterrno(): Возвращает код текущей ошибки. Например: 2.

```python
import errno

error_num = errno.geterrno()
print(error_num)
```

errno.geterror(): Возвращает описание текущей ошибки в виде строки. Например: "No such file or directory".

```python
import errno

error_desc = errno.geterror()
print(error_desc)
```
