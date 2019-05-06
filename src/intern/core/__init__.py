from sanic import Sanic
from sanic.views import HTTPMethodView
from sanic.response import text
from ..endpoint.simple_view import SimpleView
from ..endpoint.greeting import Greeting
from ..endpoint.goodbye import Goodbye


app = Sanic('some_name')


app.add_route(SimpleView.as_view(), '/simple')

app.add_route(Greeting.as_view(), '/')

app.add_route(Goodbye.as_view(), '/goodbye')


