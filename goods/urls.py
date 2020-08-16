from django. urls import path
from . import views


urlpatterns = [
    path('bed/', views.dod, name='bed'),
]