from django.urls import path, include
from dashboard import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path ('',views.home, name='home'),
    path ('accounts/profile/',views.home, name='dashboard'),
    #path ('accounts/login/' ,auth_views.LoginView.as_view(),name='login'),
    path ('accounts/login/' ,views.login_view,name='login'),
    
    path ('accounts/logout/' ,views.logout_view,name='logout'),
    path ('customers/',include('customers.urls')),
    
]
