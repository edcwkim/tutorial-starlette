from starlette.applications import Starlette

from project.routes import routes

app = Starlette(
    routes=routes,
    exception_handlers=None,
    middleware=None,
    debug=False,
)
