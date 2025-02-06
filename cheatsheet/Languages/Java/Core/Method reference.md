# :: method reference

Указание на метод без его вызова.


```java
public class MyClass {
    public static void main(String[] args) {
        MyButton button = new MyButton();
        A a = new A();
        button.reg(a::printOnClick); // Передаем ссылку на метод
        for (int i = 0; i < 5; i++) {
            button.click(); // Генерируем нажатие
            try {
                Thread.sleep(1000); // Имитация ожидания
            }
            catch (InterruptedException e) {
                e.printStackTrace();
                System.exit(1);
            }
        }
    }
}

interface IClick {
    void onClick();
}

class A {
     private int x = 10;
     public void printOnClick() {
        System.out.println("Нажата кнопка. x = " + this.x);
        this.x++;
     }
}

class MyButton {
    private IClick ic = null;
    public void reg(IClick ic) { // Регистрация обработчика
        this.ic = ic;
    }
    public void click() { // Нажатие кнопки
        if (this.ic != null) {
            this.ic.onClick();
        }
    }
}
```
