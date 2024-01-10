from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('',views.home,name="home"),
    path('menu',views.menu,name='menu'),
    path('order',views.order,name='order'),
    path('success',views.success,name='success'),
    path('signup',views.signup,name="signup"),
    path('login',views.logIn,name="login"),
    path('logout',views.logOut,name="logout"),
    path('calculator',views.calculator,name="calculator")


]
