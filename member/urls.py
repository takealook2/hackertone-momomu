from board.views import register
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),
    path('', views.register),
]