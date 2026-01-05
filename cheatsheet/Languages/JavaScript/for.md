# for

Цикл for в JavaScript используется для выполнения одного или нескольких операторов многократно, пока условие в цикле истинно
Синтаксис цикла for выглядит следующим образом:

```js
for (initialization; condition; final-expression) {
   statement(s)
}
```

|                    |                                                                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| `initialization`   | Выполняется один раз перед началом цикла<br>и обычно используется для инициализации счетчика цикла                                      |
| `condition`        | Условие, которое проверяется перед каждой итерацией цикла<br>Если условие истинно, то тело цикла выполняется,<br>иначе цикл завершается |
| `final-expression` | Выполняется после каждой итерации цикла<br>и обычно используется для изменения счетчика цикла                                           |
| `statement(s)`     | Один или несколько операторов, которые выполняются в теле цикла                                                                         |

```js
for (let i = 0; i < 5; i++) {
   console.log(i);
}
```

## Цикл по списку

```js
var myArray = [1, 2, 3, 4, 5];
for (var i = 0; i < myArray.length; i++) {
    console.log(myArray[i]);
}
// or
for (const element of myArray) {
    console.log(element);
}
```



## Цикл по словарю

### Обход только ключей (keys)

```javascript
const obj = {a: 1, b: 2, c: 3};
Object.keys(obj).forEach(key => {
    console.log(key);
});
// a, b, c
```

### Обход только значений (values)

```javascript
const obj = {a: 1, b: 2, c: 3};
Object.values(obj).forEach(value => {
    console.log(value);
});
// 1, 2, 3
```

### Обход ключей и значений (entries)

```javascript
const obj = {a: 1, b: 2, c: 3};
Object.entries(obj).forEach(([key, value]) => {
    console.log(`${key}: ${value}`);
});
// or
for (let [key, value] of Object.entries(obj)) {
    console.log(`${key}: ${value}`);
}
// or
Object.entries(obj).map(([key, value]) => {
    console.log(`${key}: ${value}`);
});
// a: 1, b: 2, c: 3
```

### `for...in` - обход всех ключей объекта

`for...in` позволяет обойти все ключи объекта (включая унаследованные)

```javascript
const obj = {a: 1, b: 2, c: 3};
for (let key in obj) {
    // Проверка чтобы избежать унаследованных свойств
    if (obj.hasOwnProperty(key)) {
        console.log(key);  // a, b, c
    }
}
```

### `reduce()` для извлечения значений или выполнения операций

Метод `reduce()` позволяет выполнять агрегирование данных при обходе объекта. Например, сложить все значения

```javascript
const obj = {a: 1, b: 2, c: 3};
// Сложим все значения
const sum = Object.values(obj).reduce((acc, value) => acc + value, 0);
console.log(sum);  // 6
```

### Получение всех ключей и значений с помощью `Object.fromEntries()`

Если вам нужно преобразовать массив пар ключ-значение обратно в объект, можно использовать `Object.fromEntries()`

```javascript
const obj = {a: 1, b: 2, c: 3};
const entries = Object.entries(obj);  // [ключ, значение]
const newObj = Object.fromEntries(entries);
console.log(newObj);  // {a: 1, b: 2, c: 3}
```
