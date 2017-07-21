import jwt

def create_token(alg='HS256', secret='secret', **data):
	return jwt.encode(data, secret, algorithm=alg)

def read_token(token, secret='secret'):
	return jwt.decode(token, secret)

token = create_token(some='data', inthe='token')
print(token)
read = read_token(token)
print(read)