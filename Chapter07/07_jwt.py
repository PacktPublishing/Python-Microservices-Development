import base64

def decode(data):

	# adding extra = for padding if needed
	pad = len(data) % 4
	if pad > 0:
		data += '=' * (4 - pad)
	return base64.urlsafe_b64decode(data)

	print[decode('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9')] 
	print[decode('eyJ1c2VyIjoidGFyZWsifQ')]
	print[decode('OeMWz6ahNsf-TKg8LQNdNMnFHNtReb0x3NMs0eY64WA')] 