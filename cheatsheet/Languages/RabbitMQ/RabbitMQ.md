### Шпаргалка по RabbitMQ 🐰📨

**RabbitMQ** — это брокер сообщений, который поддерживает протокол AMQP (Advanced Message Queuing Protocol) и используется для организации очередей сообщений между различными сервисами

## Основные понятия
### Брокер (Broker)
RabbitMQ — это сервер, который принимает, хранит и передаёт сообщения

### Очередь (Queue)
Буфер, в котором хранятся сообщения, пока они не будут обработаны

### Обменник (Exchange)
Компонент, который принимает сообщения от продюсеров и направляет их в соответствующие очереди

### Типы обменников:
- **Direct** — отправляет сообщения в очередь с определённым ключом маршрутизации (routing key)
- **Fanout** — рассылает сообщения во все привязанные очереди
- **Topic** — отправляет сообщения в очереди, соответствующие шаблону ключа маршрутизации
- **Headers** — направляет сообщения в очереди по заголовкам сообщений

### Продюсер (Producer)
Процесс, который отправляет сообщения в обменник

### Консьюмер (Consumer)
Процесс, который получает сообщения из очереди

### Связь (Binding)
Связывает очередь с обменником через ключ маршрутизации

## Установка и запуск RabbitMQ
### Установка (Ubuntu)
```sh
sudo apt update
sudo apt install rabbitmq-server -y
```

### Запуск и проверка статуса
```sh
sudo systemctl start rabbitmq-server
sudo systemctl enable rabbitmq-server
sudo systemctl status rabbitmq-server
```

### Панель управления
Включение веб-интерфейса:
```sh
sudo rabbitmq-plugins enable rabbitmq_management
```
После этого веб-интерфейс будет доступен по адресу:
📌 `http://localhost:15672`
Логин/пароль по умолчанию: `guest / guest`

## Работа с RabbitMQ через CLI
### Создать пользователя
```sh
sudo rabbitmqctl add_user myuser mypassword
```

### Выдать права
```sh
sudo rabbitmqctl set_permissions -p / myuser ".*" ".*" ".*"
```

### Посмотреть очереди
```sh
sudo rabbitmqctl list_queues
```

## RabbitMQ в Python (pika)
### Установка библиотеки
```sh
pip install pika
```

### Продюсер (отправка сообщений)
```python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Hello, RabbitMQ!')
print(" [x] Отправлено 'Hello, RabbitMQ!'")

connection.close()
```

### Консьюмер (получение сообщений)
```python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(f" [x] Получено {body.decode()}")

channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Ожидание сообщений. Для выхода нажмите CTRL+C')
channel.start_consuming()
```

## Использование обменников
### Продюсер с direct exchange
```python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

severity = 'error'
message = 'Critical error occurred!'

channel.basic_publish(exchange='direct_logs', routing_key=severity, body=message)
print(f" [x] Отправлено {severity}: {message}")

connection.close()
```

### Консьюмер с direct exchange
```python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

queue_name = channel.queue_declare(queue='', exclusive=True).method.queue
channel.queue_bind(exchange='direct_logs', queue=queue_name, routing_key='error')

def callback(ch, method, properties, body):
    print(f" [x] Получено: {body.decode()}")

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print(' [*] Ожидание сообщений...')
channel.start_consuming()
```

## Полезные команды
### Удалить очередь
```sh
sudo rabbitmqctl delete_queue myqueue
```

### Удалить пользователя
```sh
sudo rabbitmqctl delete_user myuser
```

### Очистить очередь
```sh
sudo rabbitmqctl purge_queue myqueue
```

## Полезные настройки
### Файл конфигурации (`/etc/rabbitmq/rabbitmq.conf`)
```ini
listeners.tcp.default = 5672
management.listener.port = 15672
```

### Открытие порта для удалённого доступа
```sh
sudo rabbitmqctl set_user_tags myuser administrator
sudo rabbitmqctl set_permissions -p / myuser ".*" ".*" ".*"
```

## Полезные ссылки
- [Официальная документация](https://www.rabbitmq.com/documentation.html)
- [RabbitMQ Management API](https://www.rabbitmq.com/management.html)
- [Pika (Python)](https://pika.readthedocs.io/en/stable/)

RabbitMQ отлично подходит для асинхронного обмена сообщениями и масштабируемых систем! 🚀






























### Шпаргалка по RabbitMQ

**RabbitMQ** — это брокер сообщений, реализующий модель "producer-consumer" с поддержкой очередей, маршрутизации и подтверждений доставки

## Основные понятия
### Producer (Продюсер)
Процесс, отправляющий сообщения в очередь

### Queue (Очередь)
Хранит сообщения до их обработки потребителями

### Exchange (Обменник)
Определяет правила маршрутизации сообщений в очереди

### Binding (Связка)
Связывает очередь с обменником

### Consumer (Консьюмер)
Процесс, который читает и обрабатывает сообщения из очереди

### Acknowledgment (Подтверждение)
Консьюмер подтверждает обработку сообщения, после чего оно удаляется из очереди

## Установка и запуск RabbitMQ
### Установка (Linux)
```sh
sudo apt update
sudo apt install rabbitmq-server
```

### Запуск сервиса
```sh
sudo systemctl start rabbitmq-server
```

### Проверка состояния
```sh
sudo systemctl status rabbitmq-server
```

### Включение веб-интерфейса
```sh
sudo rabbitmq-plugins enable rabbitmq_management
```
После включения интерфейс будет доступен по адресу:
👉 **http://localhost:15672** (логин/пароль: `guest/guest`)

## Работа с RabbitMQ в Python (pika)
### Установка библиотеки
```sh
pip install pika
```

### Простой продюсер
```python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

channel.queue_declare(queue="hello")

channel.basic_publish(exchange="", routing_key="hello", body="Hello, RabbitMQ!")
print(" [x] Отправлено 'Hello, RabbitMQ!'")

connection.close()
```

### Простой консьюмер
```python
import pika

def callback(ch, method, properties, body):
    print(f" [x] Получено {body.decode()}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

channel.queue_declare(queue="hello")

channel.basic_consume(queue="hello", on_message_callback=callback, auto_ack=False)

print(" [*] Ожидание сообщений. Для выхода нажмите CTRL+C")
channel.start_consuming()
```

## Exchange и маршрутизация
### Типы обменников
- **`direct`** — маршрутизация по точному совпадению ключа (routing key)
- **`fanout`** — отправка сообщения во все очереди, связанные с обменником
- **`topic`** — маршрутизация по шаблонам (`.` разделяет ключ, `*` заменяет 1 слово, `#` — любое количество слов)
- **`headers`** — маршрутизация по заголовкам

### Обменник `direct`
Продюсер:
```python
channel.exchange_declare(exchange="direct_logs", exchange_type="direct")
channel.basic_publish(exchange="direct_logs", routing_key="error", body="Ошибка в системе!")
```
Консьюмер:
```python
channel.exchange_declare(exchange="direct_logs", exchange_type="direct")
queue = channel.queue_declare(queue="", exclusive=True)
queue_name = queue.method.queue
channel.queue_bind(exchange="direct_logs", queue=queue_name, routing_key="error")
channel.start_consuming()
```

### Обменник `fanout`
Продюсер:
```python
channel.exchange_declare(exchange="logs", exchange_type="fanout")
channel.basic_publish(exchange="logs", routing_key="", body="Важное сообщение!")
```
Консьюмер:
```python
channel.exchange_declare(exchange="logs", exchange_type="fanout")
queue = channel.queue_declare(queue="", exclusive=True)
queue_name = queue.method.queue
channel.queue_bind(exchange="logs", queue=queue_name)
channel.start_consuming()
```

## Очереди с подтверждением сообщений
### Гарантированная доставка (Persistent Messages)
Чтобы сообщения не терялись при перезапуске сервера:
```python
channel.queue_declare(queue="task_queue", durable=True)
channel.basic_publish(exchange="", routing_key="task_queue", body="Hello!",
                      properties=pika.BasicProperties(delivery_mode=2))
```

### Ручное подтверждение обработки (Acknowledgment)
Чтобы сообщения не терялись, если консьюмер падает во время обработки:
```python
def callback(ch, method, properties, body):
    print(f" [x] Получено {body.decode()}")
    ch.basic_ack(delivery_tag=method.delivery_tag)
```

## Настройка QoS (Quality of Service)
Позволяет ограничить количество одновременно обрабатываемых сообщений:
```python
channel.basic_qos(prefetch_count=1)
```

## Удаление очереди
```sh
rabbitmqctl list_queues
rabbitmqctl delete_queue hello
```

## Полезные команды
### Проверить статус сервера
```sh
rabbitmqctl status
```

### Список очередей
```sh
rabbitmqctl list_queues
```

### Удалить очередь
```sh
rabbitmqctl delete_queue my_queue
```

## Полезные ссылки
- [Официальная документация](https://www.rabbitmq.com/documentation.html)
- [pika (RabbitMQ client для Python)](https://pika.readthedocs.io/)

RabbitMQ — мощный инструмент для обработки асинхронных задач, и его использование позволяет строить надёжные распределённые системы. 🚀
