from django.urls import path
from . import views

urlpatterns = [
    path('',views.login),
    path('createUser', views.new_user),
    path('login_validation', views.validateLogin),
]
