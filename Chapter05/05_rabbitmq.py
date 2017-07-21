from pika import BlockingConnection, BasicProperties

def message(topic, message):
	connection = BlockingConnection()
	try:
		channel = connection.channel()
		props = BasicProperties(content_type='text/plain', delivery_mode=1)
		channel.basic_publish('incoming', topic, message, props)
	finally:
		connection.close()

# sending a message about race 34
message('race.34', 'We have some results!')

# training 12
message('training.12', "It's time to do your long run")