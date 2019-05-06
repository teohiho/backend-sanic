from sanic import Sanic
from sanic.views import HTTPMethodView
from sanic.response import text

class SimpleView(HTTPMethodView):

  def get(self, request): 
      return text('I am get method SimpleView')

  def post(self, request):
      return text('I am post method SimpleView')

  def put(self, request):
      return text('I am put method SimpleView')

  def patch(self, request):
      return text('I am patch method SimpleView')

  def delete(self, request):
      return text('I am delete method SimpleView')