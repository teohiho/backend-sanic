from sanic import Sanic
from sanic.views import HTTPMethodView
from sanic.response import text

class Goodbye(HTTPMethodView):

  def get(self, request):
      return text('I am get method Goodbye')

  def post(self, request):
      return text('I am post method Goodbye')

  def put(self, request):
      return text('I am put method Goodbye')

  def patch(self, request):
      return text('I am patch method Goodbye')

  def delete(self, request):
      return text('I am delete method Goodbye')