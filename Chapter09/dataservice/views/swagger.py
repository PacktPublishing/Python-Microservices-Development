import os
from flakon import SwaggerBlueprint


HERE = os.path.dirname(__file__)
YML = os.path.join(HERE, '..', 'static', 'api.yaml')
api = SwaggerBlueprint('API', __name__, swagger_spec=YML)


@api.operation('getUserIds')
def get_user_ids():
    return {'one': 2}
