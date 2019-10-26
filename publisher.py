import pika
import random
import sys
import time
import string

## Assuming there are three hosts: host1, host2, and host3
node1 = pika.connection.URLParameters('amqp://admin:Admin%40123@172.19.0.3:5672/%2F')
node2 = pika.connection.URLParameters('amqp://admin:Admin%40123@172.19.0.5:5672/%2F')
node3 = pika.connection.URLParameters('amqp://admin:Admin%40123@172.19.0.4:5672/%2F')
all_endpoints = [node1, node2, node3]

while(True):
    try:
        print("Connecting...")
        ## Shuffle the hosts list before reconnecting.
        ## This can help balance connections.
        random.shuffle(all_endpoints)
        connection = pika.BlockingConnection(all_endpoints)
        channel = connection.channel()
        channel.basic_qos(prefetch_count=1)
        ## This queue is intentionally non-durable. See http://www.rabbitmq.com/ha.html#non-mirrored-queue-behavior-on-node-failure
        ## to learn more.
        channel.queue_declare('example', durable = False, auto_delete = True)

        # message = ' '.join(sys.argv[1:]) or 'Hello world!'
        message = ''.join(random.choices(string.ascii_lowercase, k=10))
        time.sleep(1)

        try:
            channel.basic_publish(exchange='',
                        routing_key='example',
                        body=message,
                        properties=pika.BasicProperties(
                            delivery_mode=2
                        ))

            print(' [x] sent %r' % message)

            connection.close()
        except KeyboardInterrupt:
            connection.close()
            break
    except pika.exceptions.ConnectionClosedByBroker:
        # Uncomment this to make the example not attempt recovery
        # from server-initiated connection closure, including
        # when the node is stopped cleanly
        #
        # break
        continue
    # Do not recover on channel errors
    except pika.exceptions.AMQPChannelError as err:
        print("Caught a channel error: {}, stopping...".format(err))
        break
    # Recover on all other connection errors
    except pika.exceptions.AMQPConnectionError as err:
        print("Connection was closed, retrying..." + str(err))
        continue
