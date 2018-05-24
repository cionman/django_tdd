from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'api'

codelab_api_router = DefaultRouter()
codelab_api_router.register(r'codelab', views.CodelabViewSet)

urlpatterns = [
    path('', include(codelab_api_router.urls))
]