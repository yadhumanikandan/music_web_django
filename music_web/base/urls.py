from django.urls import path
from . import views


app_name = "base"

urlpatterns = [
    path('', views.home, name='home'),
    path('show-scales/', views.show_scales, name='show_scales'),
    path('account/', views.account, name='account')
]
