<p>Ниже приведены основные инструкции байт-кода Python, полученные через <code>dis</code>, с кратким описанием их функций</p>
<table>
<thead>
<tr>
<th>Инструкция</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>CACHE</code></td>
<td>Используется для оптимизации локальных вызовов, сохранение промежуточных результатов</td>
</tr>
<tr>
<td><code>POP_TOP</code></td>
<td>Удаляет верхний элемент стека</td>
</tr>
<tr>
<td><code>PUSH_NULL</code></td>
<td>Помещает значение <code>None</code> на стек</td>
</tr>
<tr>
<td><code>NOP</code></td>
<td>Нет операции</td>
</tr>
<tr>
<td><code>UNARY_POSITIVE</code></td>
<td>Применяет унарный оператор <code>+</code></td>
</tr>
<tr>
<td><code>UNARY_NEGATIVE</code></td>
<td>Применяет унарный оператор <code>-</code></td>
</tr>
<tr>
<td><code>UNARY_NOT</code></td>
<td>Применяет унарный оператор <code>not</code></td>
</tr>
<tr>
<td><code>UNARY_INVERT</code></td>
<td>Применяет унарный оператор <code>~</code> (битовое инвертирование)</td>
</tr>
<tr>
<td><code>BINARY_SUBSCR</code></td>
<td>Выполняет индексирование (например, <code>a[b]</code>)</td>
</tr>
<tr>
<td><code>GET_LEN</code></td>
<td>Получает длину объекта</td>
</tr>
<tr>
<td><code>MATCH_MAPPING</code></td>
<td>Проверяет, является ли объект отображением (например, словарём)</td>
</tr>
<tr>
<td><code>MATCH_SEQUENCE</code></td>
<td>Проверяет, является ли объект последовательностью (например, списком)</td>
</tr>
<tr>
<td><code>MATCH_KEYS</code></td>
<td>Проверяет наличие ключей в словаре для сопоставления</td>
</tr>
<tr>
<td><code>PUSH_EXC_INFO</code></td>
<td>Загружает информацию об исключении</td>
</tr>
<tr>
<td><code>CHECK_EXC_MATCH</code></td>
<td>Проверяет, соответствует ли исключение указанному типу</td>
</tr>
<tr>
<td><code>CHECK_EG_MATCH</code></td>
<td>Проверяет, соответствует ли исключение типу <code>except</code> при использовании выражений "выбора"</td>
</tr>
<tr>
<td><code>WITH_EXCEPT_START</code></td>
<td>Запускает обработку блока <code>with</code></td>
</tr>
<tr>
<td><code>GET_AITER</code></td>
<td>Получает асинхронный итератор для объекта</td>
</tr>
<tr>
<td><code>GET_ANEXT</code></td>
<td>Получает следующий элемент асинхронного итератора</td>
</tr>
<tr>
<td><code>BEFORE_ASYNC_WITH</code></td>
<td>Начало асинхронного блока <code>with</code></td>
</tr>
<tr>
<td><code>BEFORE_WITH</code></td>
<td>Начало блока <code>with</code></td>
</tr>
<tr>
<td><code>END_ASYNC_FOR</code></td>
<td>Завершение асинхронного цикла <code>for</code></td>
</tr>
<tr>
<td><code>STORE_SUBSCR</code></td>
<td>Присваивает значение в индексируемый объект (например, <code>a[b] = c</code>)</td>
</tr>
<tr>
<td><code>DELETE_SUBSCR</code></td>
<td>Удаляет элемент из индексируемого объекта (например, <code>del a[b]</code>)</td>
</tr>
<tr>
<td><code>GET_ITER</code></td>
<td>Получает итератор для объекта</td>
</tr>
<tr>
<td><code>GET_YIELD_FROM_ITER</code></td>
<td>Получает итератор для выражения <code>yield from</code></td>
</tr>
<tr>
<td><code>PRINT_EXPR</code></td>
<td>Печатает результат выражения</td>
</tr>
<tr>
<td><code>LOAD_BUILD_CLASS</code></td>
<td>Загружает встроенную функцию <code>__build_class__</code> для создания класса</td>
</tr>
<tr>
<td><code>LOAD_ASSERTION_ERROR</code></td>
<td>Загружает исключение <code>AssertionError</code></td>
</tr>
<tr>
<td><code>RETURN_GENERATOR</code></td>
<td>Возвращает генератор из функции</td>
</tr>
<tr>
<td><code>LIST_TO_TUPLE</code></td>
<td>Преобразует список в кортеж</td>
</tr>
<tr>
<td><code>RETURN_VALUE</code></td>
<td>Возвращает значение из функции</td>
</tr>
<tr>
<td><code>IMPORT_STAR</code></td>
<td>Импортирует все объекты из модуля</td>
</tr>
<tr>
<td><code>SETUP_ANNOTATIONS</code></td>
<td>Устанавливает аннотации для объектов</td>
</tr>
<tr>
<td><code>YIELD_VALUE</code></td>
<td>Возвращает значение для выражения <code>yield</code></td>
</tr>
<tr>
<td><code>ASYNC_GEN_WRAP</code></td>
<td>Завершает выполнение асинхронного генератора</td>
</tr>
<tr>
<td><code>PREP_RERAISE_STAR</code></td>
<td>Подготавливает повторное возбуждение исключений в конструкции <code>except*</code></td>
</tr>
<tr>
<td><code>POP_EXCEPT</code></td>
<td>Убирает последнее исключение из стека исключений</td>
</tr>
<tr>
<td><code>STORE_NAME</code></td>
<td>Сохраняет значение в локальной переменной по имени</td>
</tr>
<tr>
<td><code>DELETE_NAME</code></td>
<td>Удаляет переменную по имени</td>
</tr>
<tr>
<td><code>UNPACK_SEQUENCE</code></td>
<td>Распаковывает значения последовательности в переменные</td>
</tr>
<tr>
<td><code>FOR_ITER</code></td>
<td>Управляет итерацией в цикле <code>for</code></td>
</tr>
<tr>
<td><code>UNPACK_EX</code></td>
<td>Распаковывает элементы последовательности с сохранением остальных в список</td>
</tr>
<tr>
<td><code>STORE_ATTR</code></td>
<td>Присваивает значение атрибуту объекта</td>
</tr>
<tr>
<td><code>DELETE_ATTR</code></td>
<td>Удаляет атрибут объекта</td>
</tr>
<tr>
<td><code>STORE_GLOBAL</code></td>
<td>Сохраняет значение в глобальной переменной</td>
</tr>
<tr>
<td><code>DELETE_GLOBAL</code></td>
<td>Удаляет глобальную переменную</td>
</tr>
<tr>
<td><code>SWAP</code></td>
<td>Меняет местами элементы стека</td>
</tr>
<tr>
<td><code>LOAD_CONST</code></td>
<td>Загружает константу (например, числа, строки)</td>
</tr>
<tr>
<td><code>LOAD_NAME</code></td>
<td>Загружает значение по имени из локальной области видимости</td>
</tr>
<tr>
<td><code>BUILD_TUPLE</code></td>
<td>Создает кортеж из элементов стека</td>
</tr>
<tr>
<td><code>BUILD_LIST</code></td>
<td>Создает список из элементов стека</td>
</tr>
<tr>
<td><code>BUILD_SET</code></td>
<td>Создает множество из элементов стека</td>
</tr>
<tr>
<td><code>BUILD_MAP</code></td>
<td>Создает словарь из элементов стека</td>
</tr>
<tr>
<td><code>LOAD_ATTR</code></td>
<td>Загружает атрибут объекта</td>
</tr>
<tr>
<td><code>COMPARE_OP</code></td>
<td>Выполняет операцию сравнения (например, <code>==</code>, <code>!=</code>)</td>
</tr>
<tr>
<td><code>IMPORT_NAME</code></td>
<td>Импортирует модуль по имени</td>
</tr>
<tr>
<td><code>IMPORT_FROM</code></td>
<td>Импортирует объект из модуля</td>
</tr>
<tr>
<td><code>JUMP_FORWARD</code></td>
<td>Переходит к указанной инструкции вперед по коду</td>
</tr>
<tr>
<td><code>JUMP_IF_FALSE_OR_POP</code></td>
<td>Если условие ложно, переходит к указанной инструкции, иначе удаляет элемент стека</td>
</tr>
<tr>
<td><code>JUMP_IF_TRUE_OR_POP</code></td>
<td>Если условие истинно, переходит к указанной инструкции, иначе удаляет элемент стека</td>
</tr>
<tr>
<td><code>POP_JUMP_FORWARD_IF_FALSE</code></td>
<td>Переходит к указанной инструкции, если условие ложно</td>
</tr>
<tr>
<td><code>POP_JUMP_FORWARD_IF_TRUE</code></td>
<td>Переходит к указанной инструкции, если условие истинно</td>
</tr>
<tr>
<td><code>LOAD_GLOBAL</code></td>
<td>Загружает глобальную переменную</td>
</tr>
<tr>
<td><code>IS_OP</code></td>
<td>Оператор сравнения <code>is</code></td>
</tr>
<tr>
<td><code>CONTAINS_OP</code></td>
<td>Оператор <code>in</code></td>
</tr>
<tr>
<td><code>RERAISE</code></td>
<td>Повторное возбуждение исключения</td>
</tr>
<tr>
<td><code>COPY</code></td>
<td>Копирует верхний элемент стека</td>
</tr>
<tr>
<td><code>BINARY_OP</code></td>
<td>Выполняет бинарную операцию (например, сложение, вычитание)</td>
</tr>
<tr>
<td><code>SEND</code></td>
<td>Отправляет значение в корутину или генератор</td>
</tr>
<tr>
<td><code>LOAD_FAST</code></td>
<td>Загружает значение из локальной переменной</td>
</tr>
<tr>
<td><code>STORE_FAST</code></td>
<td>Сохраняет значение в локальной переменной</td>
</tr>
<tr>
<td><code>DELETE_FAST</code></td>
<td>Удаляет локальную переменную</td>
</tr>
<tr>
<td><code>POP_JUMP_FORWARD_IF_NOT_NONE</code></td>
<td>Переходит к указанной инструкции, если значение не <code>None</code></td>
</tr>
<tr>
<td><code>POP_JUMP_FORWARD_IF_NONE</code></td>
<td>Переходит к указанной инструкции, если значение <code>None</code></td>
</tr>
<tr>
<td><code>RAISE_VARARGS</code></td>
<td>Вызывает исключение</td>
</tr>
<tr>
<td><code>GET_AWAITABLE</code></td>
<td>Получает объект, поддерживающий операцию <code>await</code></td>
</tr>
<tr>
<td><code>MAKE_FUNCTION</code></td>
<td>Создает объект функции</td>
</tr>
<tr>
<td><code>BUILD_SLICE</code></td>
<td>Создает объект среза</td>
</tr>
<tr>
<td><code>JUMP_BACKWARD_NO_INTERRUPT</code></td>
<td>Переходит назад в коде, не прерывая выполнение программы</td>
</tr>
<tr>
<td><code>MAKE_CELL</code></td>
<td>Создает ячейку для замыканий</td>
</tr>
<tr>
<td><code>LOAD_CLOSURE</code></td>
<td>Загружает объект замыкания</td>
</tr>
<tr>
<td><code>LOAD_DEREF</code></td>
<td>Загружает значение из ячейки замыкания</td>
</tr>
<tr>
<td><code>STORE_DEREF</code></td>
<td>Сохраняет значение в ячейке замыкания</td>
</tr>
<tr>
<td><code>DELETE_DEREF</code></td>
<td>Удаляет значение из ячейки замыкания</td>
</tr>
<tr>
<td><code>JUMP_BACKWARD</code></td>
<td>Переходит назад в коде</td>
</tr>
<tr>
<td><code>CALL_FUNCTION_EX</code></td>
<td>Вызывает функцию с аргументами, переданными в виде кортежа</td>
</tr>
<tr>
<td><code>EXTENDED_ARG</code></td>
<td>Обеспечивает поддержку длинных аргументов для инструкций</td>
</tr>
<tr>
<td><code>LIST_APPEND</code></td>
<td>Добавляет элемент в список</td>
</tr>
<tr>
<td><code>SET_ADD</code></td>
<td>Добавляет элемент во множество</td>
</tr>
<tr>
<td><code>MAP_ADD</code></td>
<td>Добавляет элемент в словарь</td>
</tr>
<tr>
<td><code>LOAD_CLASSDEREF</code></td>
<td>Загружает значение для класса, поддерживающего замыкания</td>
</tr>
<tr>
<td><code>COPY_FREE_VARS</code></td>
<td>Копирует свободные переменные для замыкания</td>
</tr>
<tr>
<td><code>RESUME</code></td>
<td>Возобновляет выполнение генератора или корутины</td>
</tr>
<tr>
<td><code>MATCH_CLASS</code></td>
<td>Сопоставляет класс при паттерн-матчинге</td>
</tr>
<tr>
<td><code>FORMAT_VALUE</code></td>
<td>Форматирует значение в строку</td>
</tr>
<tr>
<td><code>BUILD_CONST_KEY_MAP</code></td>
<td>Создает словарь из константных ключей</td>
</tr>
<tr>
<td><code>BUILD_STRING</code></td>
<td>Создает строку из элементов стека</td>
</tr>
<tr>
<td><code>LOAD_METHOD</code></td>
<td>Загружает метод объекта для вызова</td>
</tr>
<tr>
<td><code>LIST_EXTEND</code></td>
<td>Добавляет элементы в список</td>
</tr>
<tr>
<td><code>SET_UPDATE</code></td>
<td>Обновляет множество элементами</td>
</tr>
<tr>
<td><code>DICT_MERGE</code></td>
<td>Объединяет словари</td>
</tr>
<tr>
<td><code>DICT_UPDATE</code></td>
<td>Обновляет словарь новыми значениями</td>
</tr>
<tr>
<td><code>PRECALL</code></td>
<td>Подготавливает вызов функции</td>
</tr>
<tr>
<td><code>CALL</code></td>
<td>Выполняет вызов функции</td>
</tr>
<tr>
<td><code>KW_NAMES</code></td>
<td>Загружает список имен аргументов с ключевыми словами</td>
</tr>
<tr>
<td><code>POP_JUMP_BACKWARD_IF_NOT_NONE</code></td>
<td>Переходит назад, если значение не <code>None</code></td>
</tr>
<tr>
<td><code>POP_JUMP_BACKWARD_IF_NONE</code></td>
<td>Переходит назад, если значение <code>None</code></td>
</tr>
<tr>
<td><code>POP_JUMP_BACKWARD_IF_FALSE</code></td>
<td>Переходит назад, если условие ложно</td>
</tr>
<tr>
<td><code>POP_JUMP_BACKWARD_IF_TRUE</code></td>
<td>Переходит назад, если условие истинно</td>
</tr>
</tbody>
</table>