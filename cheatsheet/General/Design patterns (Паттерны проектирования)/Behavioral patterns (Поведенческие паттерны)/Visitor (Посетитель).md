# Visitor (Посетитель)

**Описание**: Позволяет добавлять новые операции к объектам без изменения их классов.
Определяет операцию, которая может быть выполнена для каждого элемента структуры объектов.

**Когда использовать**: Когда нужно выполнять операции над элементами структуры объектов, не изменяя сами элементы.

```python
class Element:
    def accept(self, visitor):
        pass

class Visitor:
    def visit_concrete_element_a(self, element):
        pass

    def visit_concrete_element_b(self, element):
        pass

class ConcreteElementA(Element):
    def accept(self, visitor):
        visitor.visit_concrete_element_a(self)

class ConcreteElementB(Element):
    def accept(self, visitor):
        visitor.visit_concrete_element_b(self)

class ConcreteVisitor(Visitor):
    def visit_concrete_element_a(self, element):
        return "Visited ConcreteElementA"

    def visit_concrete_element_b(self, element):
        return "Visited ConcreteElementB"


element_a = ConcreteElementA()
element_b = ConcreteElementB()
visitor = ConcreteVisitor()

print(visitor.visit_concrete_element_a(element_a))  # Visited ConcreteElementA
print(visitor.visit_concrete_element_b(element_b))  # Visited ConcreteElementB
```

## Example

Предположим, у нас есть разные типы документов: PDFDocument и WordDocument.
Мы хотим добавить операцию экспорта в разные форматы (например, в HTML), не изменяя сами классы документов.

```python
from abc import ABC, abstractmethod


class Document(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class PDFDocument(Document):
    def accept(self, visitor):
        visitor.visit_pdf(self)

    def pdf_specific_operation(self):
        return "PDF content"

class WordDocument(Document):
    def accept(self, visitor):
        visitor.visit_word(self)

    def word_specific_operation(self):
        return "Word content"

class Visitor(ABC):
    @abstractmethod
    def visit_pdf(self, pdf_doc):
        pass

    @abstractmethod
    def visit_word(self, word_doc):
        pass

class ExportToHTMLVisitor(Visitor):
    def visit_pdf(self, pdf_doc):
        content = pdf_doc.pdf_specific_operation()
        print(f"Exporting PDF to HTML: {content}")

    def visit_word(self, word_doc):
        content = word_doc.word_specific_operation()
        print(f"Exporting Word to HTML: {content}")


pdf_doc = PDFDocument()
word_doc = WordDocument()

visitor = ExportToHTMLVisitor()

pdf_doc.accept(visitor)
word_doc.accept(visitor)
```


### Как это работает на практике

- **Минимальные изменения в классах объектов**: Единственное, что требуется добавить в классы, - это метод `accept`.
Это небольшое изменение открывает возможность для множества новых операций (посетителей). Все остальное остается неизменным.
Это ограничение паттерна: чтобы объект мог взаимодействовать с посетителем,
он должен поддерживать механизм "принятия" посетителя через метод `accept`.
- **Легкость добавления новых операций**: Если требуется добавить новую операцию, нужно просто создать нового посетителя,
реализующего эту операцию. Сами классы объектов при этом не меняются.
Это и есть суть паттерна `Visitor` - отделение алгоритма от структуры данных.

Это позволяет разделить ответственность: сами классы объектов отвечают за свои данные и базовое поведение,
а все дополнительные операции выносятся в посетителей.
