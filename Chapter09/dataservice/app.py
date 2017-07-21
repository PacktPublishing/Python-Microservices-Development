import os
from werkzeug.exceptions import HTTPException
from flakon import create_app
from flakon.util import error_handling
from flask import request, abort, g

import jwt

from .views import blueprints
from .database import db


_HERE = os.path.dirname(__file__)
os.environ['TESTDIR'] = os.path.join(_HERE, 'tests')
_SETTINGS = os.path.join(_HERE, 'settings.ini')
app = create_app(blueprints=blueprints, settings=_SETTINGS)


with open(app.config['pub_key']) as f:
    app.config['pub_key'] = f.read()


@app.before_request
def before_req():
    authenticate(app, request)


def _400(desc):
    exc = HTTPException()
    exc.code = 400
    exc.description = desc
    return error_handling(exc)


def authenticate(app, request):
    key = request.headers.get('Authorization')
    if key is None:
        return abort(401)

    key = key.split(' ')
    if len(key) != 2:
        return abort(401)

    if key[0].lower() != 'bearer':
        return abort(401)

    pub_key = app.config['pub_key']
    try:
        token = key[1]
        token = jwt.decode(token, pub_key, audience='runnerly.io')
    except Exception as e:
        return abort(401)

    # we have the token ~ copied into the globals
    g.jwt_token = token


if __name__ == '__main__':
    db.init_app(app)
    db.create_all(app=app)
    app.run()
