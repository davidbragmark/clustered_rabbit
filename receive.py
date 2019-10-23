import pika

credentials = pika.PlainCredentials('trms', 'passwd')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbit1',
    credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='q.example')

def callback(ch, method, properties, body):
    print(' [x] Received %r' % body)


channel.basic_consume(queue='q.example',
                    auto_ack=True,
                    on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
