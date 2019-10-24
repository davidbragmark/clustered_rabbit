import pika
import sys

credentials = pika.PlainCredentials('admin', 'Admin@123')

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=credentials))

channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or 'Hello world!'

channel.basic_publish(exchange='',
                        routing_key='q.test_cluster',
                        body=message,
                        properties=pika.BasicProperties(
                            delivery_mode=2
                        ))

print(' [x] sent %r' % message)

connection.close()
