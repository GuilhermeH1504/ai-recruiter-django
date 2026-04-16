from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('analisar/',  views.nova_analise, name='nova_analise'),
]
