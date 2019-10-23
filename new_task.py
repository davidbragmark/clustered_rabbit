import sys



message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='q.example',
                      body=message)
print(" [x] Sent %r" % message)
