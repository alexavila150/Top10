from django.urls import path
from main import views

app_name = 'main'

# Implemented inferfaces
urlpatterns = [
    path('', views.index, name='index'),
]