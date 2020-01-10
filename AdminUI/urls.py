from django.contrib import admin
from .views import index,add_video, login_view, logout_view
from django.urls import path,include

urlpatterns = [
    path('',index,name='index'),
    path('add',add_video,name='add_video'),
    path('login',login_view,name='login'),
    path('logout',logout_view,name='logout'),
]