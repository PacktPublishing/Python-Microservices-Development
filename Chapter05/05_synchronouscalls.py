from requests import Session

s = Session()
s.headers['Content-Type'] = 'application/json'
s.auth = 'tarek', 'password'

# doing some calls, auth and headers are all set!
s.get('http://localhost:5000/api').json()
s.get('http://localhost:5000/api2').json()