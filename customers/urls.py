from django.urls import path, include
from customers import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path ('natural/',views.customers_view, name='customers'),
    path ('legal/',views.companies_view, name='companies'),
    path ('add_customer/',views.add_customer, name='add_customer'),
    path ('<int:id>',views.view_customer, name='view_customer'),    
    path ('edit_customer/<int:id>',views.edit_customer, name='edit_customer'),    
    path ('delete_customer/<int:id>',views.delete_customer, name='delete_customer'),    

    path ('add_company/',views.add_company, name='add_company'),
    path ('<int:id>',views.view_company, name='view_company'),    
    path ('edit_company/<int:id>',views.edit_company, name='edit_company'),    
    path ('delete_company/<int:id>',views.delete_company, name='delete_company'),    



]
