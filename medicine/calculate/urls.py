from django.urls import path
from . import views

app_name = 'calculate'

urlpatterns = [
    path('/index',views.index),
    path('/pricing',views.pricing),
]