from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    # path('activate/<uidb64>/<token>', views.activate, name='activate'),
    # path('login', views.login, name='login'),

    path('donate/', views.donate, name='donate'),

    path('signup', views.signup, name='signup'),
    # path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),    
   
]  