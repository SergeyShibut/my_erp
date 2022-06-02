from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from . import models
from . import forms

@login_required
def index(request):
    orders = models.Orders.objects.all()
    context = {

        'orders': orders,
    }
    return render(request, 'index.html', {'context': context})

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(models.Orders, id=order_id)
    requirements = models.Requirements.objects.filter(orders=order_id)
    comments = models.Comments.objects.filter(orders=order_id)

    context = {

        'order': order,
        'requirements': requirements,
        'comments': comments,

    }
    return render(request, 'order_detail.html', {'context': context})

@login_required
def add_comment(request, order_id):
    if request.method == 'POST':
        form = forms.CommentsForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            author = form.cleaned_data['author']
            order = get_object_or_404(models.Orders, id=order_id)
            models.Comments.objects.create(text=text, author=author, orders=order)
            return redirect(reverse('order_detail', args=[order_id]))

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

@login_required
def send_mail(request):
    if request.method == 'POST':
        form = forms.SendmailForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], form.cleaned_data['address'])
            if mail:
                messages.success(request, 'Письмо отправлено')
                return redirect('send_mail')
            else:
                messages.error(request, 'Ошибка отправки')

    else:
        form = forms.SendmailForm()

    return render(request, 'send_mail.html', {'form': form})

@login_required
def downloads_file(request):
    requirements = models.Requirements.objects.all()
    context = {

        'requirements': requirements,
    }
    return render(request, 'downloads_file.html', {'context': context})

@login_required
def customers_list(request):
    customers = models.Customers.objects.all()
    context = {

        'customers': customers,
    }
    return render(request, 'customers_list.html', {'context': context})

def login_view(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('orders'))
            else:
                return HttpResponse("Ошибка входа. Проверьте правильность введенных данных")

    elif request.method == 'GET':
        form = forms.LoginForm()
        context = {
            'form': form,
        }
        return render(request, 'login.html', {'context': context})


def logout_view(request):
    logout(request)
    return redirect(reverse('login'))

