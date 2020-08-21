from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('results', views.discover_computers, name='results'),
    path('make_lead', views.make_lead, name='lead'),
]
