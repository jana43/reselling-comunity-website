from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('', views.index , name = "index"),
    path('register' , views.register , name = "register"),
    path('login',views.login , name = "login"),
    path('logout_user',views.logout_user , name = "logout_user"),
    path('create',views.create , name = "create"),
] 