import pika

def publish_message(queue, body):
    # Establish a connection to the RabbitMQ server
    credentials = pika.PlainCredentials('ujvozfbg', 'wq5P1PQXkaOKGiWKrRTMBjL1FGIOGQPL')
    parameters = pika.ConnectionParameters('shark.rmq.cloudamqp.com', 5672, 'ujvozfbg', credentials)
    connection = pika.BlockingConnection(parameters)

    # Create a channel on the connection
    channel = connection.channel()

    # Declare a queue to which the message will be delivered
    channel.queue_declare(queue=queue, durable=True)

    # Publish a message to the queue
    channel.basic_publish(exchange='', routing_key=queue, body=body, properties=pika.BasicProperties(
        delivery_mode = 2))

    print(" [x] Sent '{}'".format(body))

    # Close the connection
    connection.close()