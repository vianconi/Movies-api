from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    path('', views.ExampleView.as_view(), name='ExampleView'),
]

