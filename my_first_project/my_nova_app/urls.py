from django.urls import path
from . import views

urlpatterns = [
    path('my_nova_app/', views.intro, name='intro'),
]