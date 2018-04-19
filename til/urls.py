from django.urls import path
from . import views

app_name = 'til'

urlpatterns = [
    path('', views.til, name='til'),
]