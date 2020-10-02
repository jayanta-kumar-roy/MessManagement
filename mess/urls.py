from django.urls import path
from . import views
urlpatterns = [

    path('', views.home,name='home'),
    path('allOrders/', views.allOrder,name='allOrders'),
    path('bill/', views.bill, name='bill'),

]
