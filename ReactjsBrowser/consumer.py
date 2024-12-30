import pika

def callback(ch,method,properties,body):
    print(ch,method,properties,body)


if True:
    # Use a valid URL or parameters for the RabbitMQ connection
    url = 'amqps://xjppbtxl:fRkrFhxNpkw3Dlusx8VqJpns4rI6jqze@possum.lmq.cloudamqp.com/xjppbtxl' 
    params = pika.URLParameters(url)
    # Establish a connection using the URL parameters
    connection = pika.BlockingConnection(params)
    # Create a channel
    channel = connection.channel()
    # Declare a queue (it should be the same name as used in basic_publish)
    channel.queue_declare(queue="mq_queue")
    # Publish a message to the declared queue
    channel.basic_consume(queue="mq_queue",on_message_callback=callback,auto_ack=True)
    channel.start_consuming()
    

