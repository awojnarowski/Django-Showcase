from django.urls import path

from . import views

urlpatterns = [
    path('<int:difficulty>/', views.game_select, name='game_select'),
    path('game_screen/', views.game_screen, name='game_screen'),
    path('', views.index, name='index'),
]
