import jwt

with open('pubkey.pem') as f:
	PUBKEY = f.read()

with open('privkey.pem') as f:
	PRIVKEY = f.read()

def create_token(**data):
	return jwt.encode(data, PRIVKEY, algorithm='RS512')

def read_token(token):
	return jwt.decode(token, PUBKEY)

token = create_token(some='data', inthe='token')
print(token)

read = read_token(token)
print(read)