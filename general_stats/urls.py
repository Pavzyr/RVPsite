from django.urls import path
from . import views


app_name = 'general_stats'

urlpatterns = [
    path('', views.index, name='index'),
]
