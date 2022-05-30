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
    requirements = models.Requirements.objects.filter(orders=order_id)
    comments = models.Comments.objects.filter(requirements=order_id)


    context = {

        'order': order,
        'requirements': requirements,
        'comments': comments,

    }
    return render(request, 'order_detail.html', {'context': context})

def add_comment(request, order_id):
    if request.method == 'POST':
        form = forms.CommentsForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            author = form.cleaned_data['author']
            # order = get_object_or_404(models.Orders, id=order_id)
            requirements = models.Requirements.objects.filter(orders=order_id)
            models.Comments.objects.create(text=text, author=author, requirements=requirements.orders)

    else:
        form = forms.CommentsForm()
        order = get_object_or_404(models.Orders, id=order_id)
        requirements = models.Requirements.objects.filter(orders=order_id)

        context = {

            'form': form,
            'order': order,
            'requirements': requirements,
        }
        return render(request, 'add_comment.html', {'context': context})
