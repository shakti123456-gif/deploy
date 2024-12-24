import pika

def publish_message(message):
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
    channel.basic_publish(exchange="", routing_key="mq_queue", body=message)
    # Close the channel and connection
    channel.close()
    connection.close()
    
