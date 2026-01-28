from django.urls import path
from . import views

urlpatterns = [
    path('my_nova_app/', views.my_nova_app, name='intro'),
    path('my_nova_app/more/<int:id>/', views.details, name='details'),
]