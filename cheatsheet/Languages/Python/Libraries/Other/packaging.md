Библиотека `packaging` в Python используется для работы с упаковкой и распаковкой пакетов, а также для управления метаданными пакетов
Она предоставляет функции для создания, проверки, обновления и распаковки пакетов в формате wheel или в формате сжатого архива

Методы и подмодули:

## packaging.version
`parse(version_string)`: Парсит версию из строки и возвращает объект `Version`
`Version`: Класс для представления версии пакета

## packaging.specifiers
`Specifier`: Класс для представления спецификации версии пакета.
`LegacySpecifier`: Класс для представления устаревшей спецификации версии пакета
`SpecifierSet`: Класс для представления набора спецификаций версий пакета

## packaging.requirements
`Requirement`: Класс для представления требования к пакету

## packaging.markers
`Marker`: Класс для представления условий маркера
`default_environment`: Возвращает стандартное окружение

## packaging.tags
`Tag`: Класс для представления метки платформы
`sys_tags()`: Возвращает метки платформы для текущей системы

Наиболее часто используемые методы в библиотеке `packaging`

### parse(version_string)
Парсит версию из строки и возвращает объект `Version`
```python
from packaging import version

version_string = "1.2.3"
parsed_version = version.parse(version_string)
print(parsed_version)
```

### SpecifierSet(specifier_string)
Создает набор спецификаций версий на основе строки
```python
from packaging.specifiers import SpecifierSet

specifier_string = ">=1.0,<=2.0"
specifier_set = SpecifierSet(specifier_string)
print(specifier_set)
```

### Requirement(requirement_string)
Создает требование к пакету на основе строки
```python
from packaging.requirements import Requirement

requirement_string = "numpy>=1.0"
requirement = Requirement(requirement_string)
print(requirement)
```
