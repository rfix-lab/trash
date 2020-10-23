import pika

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

def main():
    credentials = pika.PlainCredentials('mqadmin', 'mqadmin')
    parameters = pika.ConnectionParameters('10.176.15.27', 5672, '/', credentials)
    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()

    channel.queue_declare(queue='PSqueue')

    channel.basic_consume(
        queue='PSqueue', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

main()