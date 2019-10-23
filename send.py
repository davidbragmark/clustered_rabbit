import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbit1'))
channel = connection.channel()

channel.queue_declare(queue='q.example')

channel.basic_publish(exchange='',
                        routing_key='example',
                        body='Hello World! testing message.')

print(' [x] sent hello world! message')

connection.close()
