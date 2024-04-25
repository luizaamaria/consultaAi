from django.urls import path
from .views import consulta_cep

urlpatterns = [
    path('consulta', consulta_cep, name='consulta_cep'),
]