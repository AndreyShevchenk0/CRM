from django. urls import path
from . import views


urlpatterns = [
    path('voronka/', views.red, name='base'),
]