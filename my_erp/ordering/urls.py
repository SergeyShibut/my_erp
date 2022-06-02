from django.urls import path
from . import views

urlpatterns = [

    path('login', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.index, name='orders'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('add_comment/<int:order_id>/', views.add_comment, name='add_comment'),
    path('send_mail', views.send_mail, name='send_mail'),
    path('downloads_file', views.downloads_file, name='downloads_file'),
    path('customers_list', views.customers_list, name='customers_list'),





]