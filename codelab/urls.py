from django.urls import path
from . import views

app_name = 'codelab'

urlpatterns = [
    path('', views.get_codelab_list, name='list'),
    path('new/', views.create_codelab, name='create'),
    path('new/detail/', views.create_codelab_detail, name='create_detail'),
    path('update/<int:pk>/', views.update_codelab, name='update'),
    path('update/<slug:slug>/', views.update_codelab_detail, name='update_detail'),
    path('<int:pk>/', views.get_codelab, name='codelab'),
    path('<slug:slug>/'
         , views.get_codelab_detail, name='codelab_detail'),
]