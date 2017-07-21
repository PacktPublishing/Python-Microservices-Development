import pika
from pika import BlockingConnection, BasicProperties

def on_message(channel, method_frame, header_frame, body):
	race_id = method_frame.routing_key.split('.')[-1]
	print('Race #%s: %s' % (race_id, body))
	channel.basic_ack(delivery_tag=method_frame.delivery_tag)

print("Race NEWS!")
print("Race #34: b'We have some results")
connection = pika.BlockingConnection()
channel = connection.channel()
#channel.basic_consume(on_message, queue='race')
try:
	channel.start_consuming()
except KeyboardInterrupt:
	channel.stop_consuming()

connection.close()