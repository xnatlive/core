from django.urls import path, include
from customers import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path ('',views.customers_view, name='customers'),
    path ('add_customer/',views.add_customer, name='add_customer'),

    
]
