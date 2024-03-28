from django.urls import path
from .views import (
    criar_vacina,
)

urlpatterns = [
    path('criar_vacina', criar_vacina, name='criar_vacina'),
]
