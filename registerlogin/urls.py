from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),  # Asegúrate de que `views.home` esté definido en core/views.py
]