from flakon import JsonBlueprint


home = JsonBlueprint('api', __name__)


@home.route('/')
def some():
    return {'here': 1}
