from django.http import HttpResponse
from .models import Shipments

from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from django.template import loader

def index(request):
    ship_list = Shipments.objects.order_by('id')
    context = {
        'ship_list': ship_list,
    }
    return render(request, 'shipcomp/index.html', context)

def shipments_detail_view(request):

    shpmnt = Shipments.objects.get(all)
    context = {
        'warehouse': shpmnt.warehouse,
        'dis_cntr': shpmnt.dist_center,
        'ship_weight': shpmnt.shipping_weight,

    }
    return render(request, 'shipcomp/shipment_list.html', {'shipment': shpmnt})

class ShipmentListView(ListView):
    template = 'shipcomp/shipment_list.html'
    queryset = Shipments.objects.all()