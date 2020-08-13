from django. urls import path
from . import views

urlpatterns = [
    path('', views.mod, name='base'),
    #path('myJob/', views.xer, name='myJob'),
]