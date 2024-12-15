from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Zde můžete přidat další URL vzory, pokud je budete potřebovat
]