from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_home,name="admin_home"),
    path('login', views.my_login,name="my_login"),
    path('register', views.register,name="register"),
    path('create/players', views.create_players,name="create_players"),
    path('create/match', views.create_match,name="create_match"),
    path('create/team', views.create_team,name="create_team"),
]
