from django.urls import path
from .views import register, register_handle

urlpatterns = [
    path('register/', register, name='register'),
    path('register_handle', register_handle, name='register_handle'),

]
