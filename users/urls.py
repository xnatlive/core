from django.urls import path, include
from users import views

urlpatterns = [
    path ('login_user', views.login_user,name='login'),
    path ('logout_user', views.logout,name='logout'),
    
]
