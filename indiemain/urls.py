from django.urls import path
from . import views

urlpatterns = [
    path('', views.indie_main, name='indie_main'),
]