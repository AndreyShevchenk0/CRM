from django. urls import path
from . import views


urlpatterns = [
    path('bis/', views.dod, name='bs'),
]