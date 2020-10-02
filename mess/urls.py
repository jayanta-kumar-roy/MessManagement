from django.urls import path
from . import views
urlpatterns = [

    path('register/',views.registerPage,name='register'),
    path('login/',views.loginPage,name='login'),
    path('', views.home,name='home'),
    path('allOrders/', views.allOrder,name='allOrders'),
    path('bill/', views.bill, name='bill'),
    path('placeOrder/',views.placeOrder,name='placeOrder')

]
