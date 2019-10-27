from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.views.generic.base import RedirectView

from . import views
urlpatterns = [

    path('',views.index,name="index"),
    path('movie_list/',views.Movie_list,name="movie_list"),
    path('movie_details/<int:pk>/',views.Movie_details,name="movie_details"),
    path('create_list/',views.Create_list,name="create_list"),
    path('view_movie_list/',views.View_movie_list,name="view_movie_list"),
    path('view_movie_list_details/<int:pk>/', views.View_movie_list_details, name="view_movie_list_details"),

]