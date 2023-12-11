# movie_recommendation_app/urls.py
from django.urls import path
from .views import signup, login_view, movie_recommendation 

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('home/', movie_recommendation, name='movie_recommendation'),
]
