```java
public interface InterfaceName {

}
```
```java
public interface InterfaceName extends Interface2Name, Interface3Name {

}
```
```java
public class ClassName implements InterfaceName, Interface2Name {

}
```

- Методы `public abstract`
- Поля `public final static`

# Статические константы

Помимо сигнатур методов, в блоке интерфейса можно создавать общедоступные статические константы
Так как создать допускается только статические константы, ключевые слова `static` и `final` обычно не указываются
Константы просто наследуются классом и доступны через название класса или через название интерфейса

# Статические методы

Внутри блока интерфейса можно определить статические методы с реализацией
Такие методы доступны внутри блока интерфейса, а также через название интерфейса
Переопределить такие методы внутри класса **нельзя**, и через экземпляр класса или название класса они **недоступны**

```java
interface IStatic {
    static void test() {
        print();
    }

    static void print() {
        System.out.println("Привет");
    }
}

class K implements IStatic {
    public K() {
        IStatic.test();
    }
}

public class MyClass {
    public static void main(String[] args) {
        K k = new K(); // Привет
        IStatic.print(); // Привет
    }
}
```

# Методы по умолчанию

Позволяет добавить новый метод и сразу реализовать блок с кодом
Классы могут переопределить метод по умолчанию
Метод по умолчанию объявляется с помощью ключевого слова `default`

```java
interface IDefault {
    default void print() {
        System.out.println("Привет");
    }
}

class L implements IDefault {

}

class M implements IDefault {
    @Override
    public void print() {
        System.out.println("Прощай");
    }
}

public class MyClass {
    public static void main(String[] args) {
        L obj = new L();
        obj.print(); // Привет
        M obj2 = new M();
        obj2.print(); // Прощай
    }
}
```

## Коллизия имён

```java
interface IDefault2 {
    default void print() {
        System.out.println("Привет, Вася");
    }
}

class N implements IDefault, IDefault2 {
    @Override
    public void print() {
        IDefault.super.print();
        IDefault2.super.print();
    }
}

public class MyClass {
    public static void main(String[] args) {
        N obj = new N();
        obj.print(); // Привет
                     // Привет, Вася
    }
}
```


### Example

```java
public interface ILights {
    boolean isOn = false;
    void setLight (boolean set);
}
```

```java
interface MyInterface {
    int MY_CONSTANT = 10;

    default void defaultMethod(String argument) {
        System.out.println("Value of argument: " + argument);
        System.out.println("Value of MY_CONSTANT: " + MY_CONSTANT);
    }
}

class MyClass implements MyInterface {}

public class Main {
    public static void main(String[] args) {
        MyClass myObject = new MyClass();
        myObject.defaultMethod("Text");
        // Value of argument: Text
        // Value of MY_CONSTANT: 10
    }
}
```
