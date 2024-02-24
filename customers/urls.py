from django.urls import path, include
from customers import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path ('natural/',views.customers_view, name='customers'),
    path ('legal/',views.companies_view, name='companies'),
    path ('add_customer/',views.add_customer, name='add_customer'),
    path ('add_company/',views.add_customer, name='add_company'),

    
]
