from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from . import models
from . import forms

def index(request):
    orders = models.Orders.objects.all()
    context = {

        'orders': orders,
    }
    return render(request, 'index.html', {'context': context})

def order_detail(request, order_id):
    order = get_object_or_404(models.Orders, id=order_id)
    requirements = models.Requirements.objects.filter(order=order_id)


    context = {

        'order': order,
        'requirements': requirements,

    }
    return render(request, 'order_detail.html', {'context': context})