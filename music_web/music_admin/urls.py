from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('add_scale/', views.add_scale, name='add_scale'),
]