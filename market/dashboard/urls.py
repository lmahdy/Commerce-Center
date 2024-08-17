from django.urls import path

from . import views

app_name = 'dashboard'#we are setting the app_name to dashboard so that we can use it to refer to the dashboard app in the templates exemple: {% url 'dashboard:index' %}

urlpatterns = [
    path('', views.index, name='index'),
]