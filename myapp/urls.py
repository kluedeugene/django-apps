
from django.urls import path
from myapp import views


urlpatterns = [
    path('', views.index),
    path('create/', views.index),
    path('read/<id>/', views.read)
]
