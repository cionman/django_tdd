from django.urls import path
from . import views

app_name = 'toy'

urlpatterns = [
    path('', views.create_toy, name='toy'),
]