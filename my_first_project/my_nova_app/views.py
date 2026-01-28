from django.http import HttpResponse
from django.template import loader
from .models import Person

def my_nova_app(request):
  persons = Person.objects.all().values()
  template = loader.get_template('persons.html')
  context = {
    'persons': persons,
  } 
  return HttpResponse(template.render(context, request))

def details(request, id):
  persons = Person.objects.get(id=id)
  template = loader.get_template('more.html')
  context = {
    'persons': persons,
  }
  return HttpResponse(template.render(context, request))


# Create your views here.
