# Proxy (Заместитель)

**Описание**: Представляет собой объект-заместитель, который контролирует доступ к другому объекту

**Когда использовать**: Когда нужно управлять доступом к объекту, например, для ленивой инициализации, контроля доступа или логирования

```python
class RealSubject:
    def request(self):
        return "RealSubject: Handling request."

class Proxy:
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        print("Proxy: Checking access before forwarding request.")
        return self._real_subject.request()

real_subject = RealSubject()
proxy = Proxy(real_subject)
print(proxy.request())
# Proxy: Checking access before forwarding request.
# RealSubject: Handling request.
```
