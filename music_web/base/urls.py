from django.urls import path
from . import views


app_name = "base"

urlpatterns = [
    path('', views.home, name='home'),
    path('scales/', views.show_scales, name='show_scales'),
    path('chords/', views.show_chords, name='show_chords'),
    path('scales/<int:id>', views.show_scale_result, name='show_scale_result'),
    path('chords/<int:id>', views.show_chord_result, name='show_chord_result'),
    path('account/', views.account, name='account'),
    path('news_letter/', views.news_letter, name='news_letter')
]
