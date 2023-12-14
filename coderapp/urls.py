
from django.urls import path
from . import views

urlpatterns = [
    path('profesores/', views.leer_profesor ),
    path('alumnos/', views.leer_alumnos),
]
