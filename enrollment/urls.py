from django.urls import path
from . import views

app_name = 'enrollment'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('register/create/', views.register_create, name='register_create'),
]