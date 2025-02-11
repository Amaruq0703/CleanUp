from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index, name='index'),
    path('login/', view=views.login, name='login'),
    path('signUp/', view=views.signup, name='signup'),
    path('home/', view=views.home, name='home'),
]