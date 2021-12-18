from django.urls import path
from . import views
from .views import ShipmentListView, shipments_detail_view

urlpatterns = [
    path('', views.index, name='index'),
    path('/shipments', views.shipments_detail_view, name='shipments')
]
# Create your views here.
