from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('guest-list/', views.guestList, name='guest-list'),
    path('guest-detail/<str:pk>/', views.guestDetail, name='guest-detail'),
    path('guest-create/', views.guestCreate, name='guest-create'),
    path('guest-update/<str:pk>/', views.guestUpdate, name='guest-update'),
    path('guest-delete/<str:pk>/', views.guestDelete, name='guest-delete'),
]