Библиотека "resource" в Python используется для доступа и управления системными ресурсами, такими как время CPU, память и дескрипторы файлов

Методы и подмодули модуля "resource":

`getrusage(who)` - возвращает информацию о системных ресурсах для указанного процесса или группы процессов
`getrlimit(resource)` - получает текущие ограничения на указанный ресурс
`setrlimit(resource, limits)` - устанавливает ограничения на указанный ресурс
`getpagesize()` - возвращает размер страницы памяти операционной системы
`getrusage()` - возвращает информацию о системных ресурсах для текущего процесса
`RUSAGE_SELF` - константа, указывающая на текущий процесс
`RUSAGE_CHILDREN` - константа, указывающая на дочерние процессы текущего процесса

Наиболее часто используемые методы:

`getrusage(who)` - получает информацию о системных ресурсах для указанного процесса или группы процессов

```python
import resource

usage = resource.getrusage(resource.RUSAGE_SELF)
print(usage)
```

`getrlimit(resource)` - получает текущие ограничения на указанный ресурс

```python
import resource

limit = resource.getrlimit(resource.RLIMIT_CPU)
print(limit)
```

`setrlimit(resource, limits)` - устанавливает ограничения на указанный ресурс

```python
import resource

# Ограничение на время CPU - 2 секунды
limits = (2, resource.RLIM_INFINITY)
resource.setrlimit(resource.RLIMIT_CPU, limits)
```
