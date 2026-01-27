from django.urls import path
from .views import NoticiaListAPIView

urlpatterns = [
    path('informe', view=NoticiaListAPIView.as_view(), name="listar_noticias")
    
]