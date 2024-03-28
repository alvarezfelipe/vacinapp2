from django.urls import path
from .views import *

urlpatterns = [
    path('', cliente_home, name='cliente_home'),
]
