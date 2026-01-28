from django.http import HttpResponse
from django.template import loader

def my_nova_app(request):
  persos = Item.objects.all().values()
  template = loader.get_template('all_items.html')
  context = {
    'myitems': myitems,
  }
  return HttpResponse(template.render(context, request))


# Create your views here.
