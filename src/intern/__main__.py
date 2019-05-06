from .core import app
from .endpoint.simple_view import SimpleView
from .endpoint.greeting import Greeting
from .endpoint.goodbye import Goodbye


app.add_route(SimpleView.as_view(), '/simple')

app.add_route(Greeting.as_view(), '/')

app.add_route(Goodbye.as_view(), '/goodbye')

app.run(host='0.0.0.0', port=8888)