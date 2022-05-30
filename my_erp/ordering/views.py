from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail

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
            order = get_object_or_404(models.Orders, id=order_id)
            requirements = models.Requirements.objects.filter(orders=order_id)
            models.Comments.objects.create(text=text, author=author, )
            return redirect('order_detail')

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


def send_mail(request):
    if request.method == 'POST':
        form = forms.SendmailForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], form.cleaned_data[
                'your_address'],form.cleaned_data['address'])
            if mail:
                messages.success(request, 'Письмо отправлено')
                return redirect('send_mail')
            else:
                messages.error(request, 'Ошибка отправки')

    else:
        form = forms.SendmailForm()

    return render(request, 'send_mail.html', {'form': form})
