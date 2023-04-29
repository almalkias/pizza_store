from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
      path('selectPizza/', views.Type_of_Pizza, name='selectPizza'),
]
