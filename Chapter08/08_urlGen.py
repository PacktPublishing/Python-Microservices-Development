from stravalib.client import Client
def get_strava_url():
	client = Client()
	cid = app.config['STRAVA_CLIENT_ID']
	redirect = app.config['STRAVA_REDIRECT']
	url = client.authorization_url(client_id=cid, redirect_uri=redirect)
	print(url)