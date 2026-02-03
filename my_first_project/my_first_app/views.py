from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Item

# Create your views here.
def my_first_app(request):
  myitems = Item.objects.all().values()
  template = loader.get_template('all_items.html')
  context = {
    'myitems': myitems,
  }
  return HttpResponse(template.render(context, request))

def details(request,id):
  myitems = Item.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'myitems': myitems,
  }
  return HttpResponse(template.render(context, request))


def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  myitems = Item.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'myitems' : myitems,
    #'firstname': 'Rasheedah',
  }
  return HttpResponse(template.render(context, request))