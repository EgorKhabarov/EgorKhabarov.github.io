```java
import java.util.function.Function;

Function<Integer, Integer> f = (Integer n) -> n * 2;
int x = f.apply(20);
System.out.println(x); // 40
```

мы не можем использовать элементарные типы следует использовать классы-«обертки» над элементарными типами



```java
class Box <T> {
    private T obj;
    public Box(T obj) {
        this.setObj(obj);
    }
    public T getObj() {
        return obj;
    }
    public void setObj(T obj) {
        this.obj = obj;
    }
}
```
```java
Box<String> box = new Box<String>("Строка"); // или new Box<>("Строка");
box.setObj("Строка 2"); // OK
// box.setObj(10); // Ошибка
String s = box.getObj();
System.out.println(s); // Строка 2
```

Можно указать сразу несколько типов

```java
class ClassB <T1, T2> {
    public T1 obj1;
    public T2 obj2;
    public T2 obj3;
    int x;

    public ClassB(T1 obj1, T2 obj2, T2 obj3, int x) {
        this.obj1 = obj1;
        this.obj2 = obj2;
        this.obj3 = obj3;
        this.x = x;
    }
}
```
```java
ClassB<Integer, Double> c = new ClassB<Integer, Double>(10, 1.5, 45.9, 8);
System.out.println(c.obj1); // 10
System.out.println(c.obj2); // 1.5
System.out.println(c.obj3); // 45.9
System.out.println(c.x); // 8
// ClassB<Integer, Double> c = new ClassB<Integer, Integer>(10, 1.5, 45.9, 8); // Ошибка
```

# Ограничения

При объявлении типа можно сразу ограничить его названием базового класса или интерфейса
Для этого используется улючевое слово `extends`
```java
class ClassA <T extends Number> {
    public T obj;

    public ClassA(T obj) {
        this.obj = obj;
    }
}
```


Класс `Number` является базовым для классов `Integer` и `Double`, поэтому мы можем их использовать вместо обобщенного типа
```java
ClassA<Integer> c1 = new ClassA<Integer>(10);
System.out.println(c1.obj); // 10
ClassA<Double> c2 = new ClassA<Double>(10.5);
System.out.println(c2.obj); // 10.5
// класс `Date` не является наследником Number
// ClassA<Date> c = new ClassA<Date>(new Date()); // Ошибка!
```
Мы можем ограничить тип несколькими интерфейсами
В этом случае они перечисляются через символ `&`
```java
public class MyClass {
    public static void main(String[] args) {
        ClassA<A> c = new ClassA<A>(new A());
        c.test();
    }
}
interface ITest1 {
    void test1();
}
interface ITest2 {
    void test2();
}
class A implements ITest1, ITest2 {
    @Override
    public void test1() {
        System.out.println("test1()");
    }
    @Override
    public void test2() {
        System.out.println("test2()");
    }
}
class ClassA <T extends ITest1 & ITest2> {
    public T obj;

    public ClassA(T obj) {
        this.obj = obj;
    }
    public void test() {
        this.obj.test1();
        this.obj.test2();
    }
}
```

# Методы

Если метод является статическим, то обобщенный тип, объявленный в заголовке обобщенного класса, внутри статического метода использовать нельзя
```
[Модификатор] static <Обобщенный_тип> Тип_результата Название_метода(Параметры) {

}
Класс.<Тип>Название_метода(Значения)
Класс.Название_метода(Значения)
```


```java
public class MyClass {
    public static void main(String[] args) {
        MyClass.<Integer>print(10);
        MyClass.<String>print("Строка");
        MyClass.print(10);
        MyClass.print("Строка");
        A obj = new A();
        MyClass.<A>echo(obj);
        MyClass.echo(obj);
    }
    public static <T> void print(T obj) {
        System.out.println(obj.toString());
    }
    // Ограничение интерфейсом ITest
    public static <T extends ITest> void echo(T obj) {
        Обобщенные типы 333
        obj.print(); // Вызов метода из интерфейса
    }
}
interface ITest {
    void print();
}
class A implements ITest {
    private int x = 20;
    @Override
    public void print() {
    System.out.println("x = " + this.x);
    }
}
```
Внутри обычных методов, а также в качестве типа параметров и типа возвращаемого значения, мы можем использовать обобщенный тип, объявленный в заголовке обобщенного класса
Кроме того, мы можем дополнительно указать обобщенный тип, как и в случае со статическим обобщенным методом
Причем, обобщенные обычные методы могут быть как внутри обобщенного класса, так и внутри обычного класса

```java
public class MyClass {
    public static void main(String[] args) {
        A obj1 = new A();
        obj1.<Integer>print(10);
        obj1.print(10);
        B<Integer> obj2 = new B<Integer>(50);
        obj2.<String>print(10, "строка");
        obj2.print(10, "строка");
    }
}
class A {
    // Обобщенный метод внутри обычного класса
    public <T> void print(T obj) {
        System.out.println(obj.toString());
    }
}
class B <T> {
    private T obj;
    // Обобщенный тип в параметре конструктора
    public B(T obj) {
        this.obj = obj;
    }
    // Дополнительный обобщенный тип
    public <U> void print(T obj1, U obj2) {
        System.out.println(obj1.toString());
        System.out.println(obj2.toString());
        System.out.println(this.obj.toString());
    }
}
```

# Маски типов

При передаче объектов дженерик классов в качестве значения параметра метода, а также при объявлении переменной, можно использовать следующие конструкции

|                         |                                      |
|-------------------------|--------------------------------------|
| `<?>`                   | Любой тип                            |
| `<? extends T>`         | Класс Класс и все производные классы |
| `<? super Класс или T>` | Класс Класс и все базовые классы     |


# Интерфесы

```java
interface ITest1 <T> {
    void test(T t);
}
class A <T> implements ITest1 <T> {
    private T obj;

    public A(T obj) {
        this.obj = obj;
    }
    public T getObj() {
        return this.obj;
    }
    @Override
    public void test(T t) {
        System.out.println("A obj = " + this.obj);
        System.out.println("t = " + t);
    }
}
```

При объявлении переменной можно указать как тип класса, так и тип интерфейса:
```java
A<Integer> obj1 = new A<Integer>(10);
obj1.test(15);
ITest1<Integer> obj2 = new A<Integer>(33);
obj2.test(81);
```

```java
interface ITest2 <T, U> {
    void test1(T t);
    void test2(U u);
}

class B <T, U> implements ITest2 <T, U> {
    private T obj;

    public B(T obj) {
        this.obj = obj;
    }
    public T getObj() {
        return this.obj;
    }
    @Override
    public void test1(T t) {
        System.out.println("t = " + t);
    }
    @Override
    public void test2(U u) {
        System.out.println("u = " + u);
    }
}
```

```java
B<Integer, Double> obj1 = new B<Integer, Double>(10);
obj1.test1(15);
obj1.test2(20.5);
ITest2<Integer, Double> obj2 = new B<Integer, Double>(10);
obj2.test1(88);
obj2.test2(85.5);
```

Предыдущие классы были все обобщенными
Однако и простой класс может реализовать обобщенный интерфейс
Для этого при объявлении класса вместо обобщенного типа указывается реальный тип
Создадим обычный класс C, реализующий интерфейс `ITest1<T>`

```java
class C implements ITest1 <Integer> {
    private int obj;

    public C(int obj) {
        this.obj = obj;
    }
    public int getObj() {
        return this.obj;
    }
    @Override
    public void test(Integer t) {
        System.out.println("C obj = " + this.obj);
        System.out.println("t = " + t);
    }
}
```

```java
C obj1 = new C(10);
obj1.test(15);
ITest1<Integer> obj2 = new C(20);
obj2.test(88);
```

Обратите внимание: после названия интерфейса внутри угловых скобок необходимо указать реальный тип, совпадающий с типом, указанным при объявлении класса `C`

```java
A<Integer> obj1 = new A<Integer>(10);
A<Double> obj2 = new A<Double>(33.5);
System.out.println(obj1.getClass()); // class A
System.out.println(obj2.getClass()); // class A
```
Классы `A<Integer>` и `A<Double>` компилятор превращает в «сырой» класс `A`
Бессмысленно сравнивать эти классы с помощью оператора `instanceof` он всегда вернет истину, т. к. это один и тот же «сырой» класс `A`
Компилятор даже не позволит их сравнивать
Только, если вместо реального типа подставить маску `<?>`
