from sanic import Sanic
from sanic.views import HTTPMethodView
from sanic.response import text

class Greeting(HTTPMethodView):

  def get(self, request):
      return text('I am get method Greeting')

  def post(self, request):
      return text('I am post method Greeting')

  def put(self, request):
      return text('I am put method Greeting')

  def patch(self, request):
      return text('I am patch method Greeting')

  def delete(self, request):
      return text('I am delete method Greeting')