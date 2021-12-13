from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
# Create your views here.
