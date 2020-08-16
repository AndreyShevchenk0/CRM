from django. urls import path
from . import views


urlpatterns = [
    path('dok/', views.dod, name='bed'),
]