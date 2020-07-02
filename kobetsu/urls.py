from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('participate', views.participate, name='participate'),
    path('wait', views.wait, name='wait'),
    path('next', views.next, name='next'),
    ]



