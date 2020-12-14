from starlette.routing import Route

from . import endpoints

routes = [
    Route('/', endpoints.Homepage),
    Route('/user/{username}', endpoints.User),
]
