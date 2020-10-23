import pika

def main():
    credentials = pika.PlainCredentials('mqadmin', 'mqadmin')
    parameters = pika.ConnectionParameters('10.176.15.27', 5672, '/', credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue='PSqueue')

    #while True:
    channel.basic_publish(exchange='', routing_key='PSqueue', body='Ya-hooo!')
    print(" [x] Sent 'Ya-hooo!'")


    connection.close()

main()