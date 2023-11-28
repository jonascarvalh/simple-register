from django.urls import path
from . import views

app_name = 'enrollmennt'

urlpatterns = [
    path('', views.register_view, name='register')
]