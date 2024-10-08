from django.urls import path
from . import views


app_name = "music_admin"

urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('add_scale/', views.add_scale, name='add_scale'),
    path('add_chord/', views.add_chord, name='add_chord'),
    # path('show_db/', views.show_db, name='show_db'),
]
