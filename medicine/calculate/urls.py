from django.urls import path
from . import views

app_name = 'calculate'

urlpatterns = [
    path('/medicine',views.medicine),
    path('/init',views.init),
]