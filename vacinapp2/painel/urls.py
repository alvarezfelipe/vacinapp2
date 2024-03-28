from django.urls import path
from .views import *

urlpatterns = [
    path('', painel_home, name='painel_home'),
]