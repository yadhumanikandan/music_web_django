from django.urls import path
from . import views


app_name = "base"

urlpatterns = [
    path('', views.home, name='home'),
    path('scales/', views.show_scales, name='show_scales'),
    path('scales/<int:id>', views.show_result, name='show_result'),
    path('account/', views.account, name='account')
]
