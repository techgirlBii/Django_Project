from django.urls import path
from . import views

urlpatterns= [
    path('', views.main, name='main'),
    path('my_first_app/' , views.my_first_app, name='my_first_app'),
    path('my_first_app/details/<int:id>/' , views.details, name='details'),
    path('testing/' , views.testing, name='testing'),
    
]