import time
from flask import request, current_app, abort, jsonify
from werkzeug.exceptions import HTTPException
from flakon import JsonBlueprint
from flakon.util import error_handling

import jwt


home = JsonBlueprint('home', __name__)


def _400(desc):
    exc = HTTPException()
    exc.code = 400
    exc.description = desc
    return error_handling(exc)


@home.route('/.well-known/jwks.json')
def _jwks():
    """Returns the public key in the Json Web Key (JWK) format
    """
    key = {"alg": "RS512",
           "e": "AQAB",
           "n": current_app.config['pub_key'],
           "kty": "RSA",
           "use": "sig"}

    return jsonify([key])


_SECRETS = {'strava': 'f0fdeb1f1584fd5431c4250b2e859457'}


def is_authorized_app(client_id, client_secret):
    return _SECRETS.get(client_id) == client_secret


@home.route('/oauth/token', methods=['POST'])
def create_token():
    key = current_app.config['priv_key']
    try:
        data = request.form
        if data.get('grant_type') != 'client_credentials':
            return _400('Wrong grant_type')

        client_id = data.get('client_id')
        client_secret = data.get('client_secret')
        aud = data.get('audience', '')

        if not is_authorized_app(client_id, client_secret):
            return abort(401)

        now = int(time.time())

        token = {'iss': 'runnerly-tokendealer',
                 'aud': aud,
                 'iat': now,
                 'exp': now + 3600 * 24}
        token = jwt.encode(token, key, algorithm='RS512')
        return {'access_token': token.decode('utf8')}
    except Exception as e:
        return _400(str(e))


@home.route('/verify_token', methods=['POST'])
def verify_token():
    key = current_app.config['pub_key']
    try:
        token = request.json['access_token']
        audience = request.json.get('audience', '')
        return jwt.decode(token, key, audience=audience)
    except Exception as e:
        return _400(str(e))
