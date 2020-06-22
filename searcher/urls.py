from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('results', views.discover_computers, name='results'),
]