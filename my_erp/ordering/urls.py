from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='orders'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('add_comment/<int:order_id>/', views.add_comment, name='add_comment'),



]