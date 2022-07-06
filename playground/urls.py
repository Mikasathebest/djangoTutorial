from django.urls import path
from . import views

# Url conf
urlpatterns = [
    path('hello/', views.say_hello)
]