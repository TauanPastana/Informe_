from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, filters
from .models import News_Informe
from .serializer import News_Serializer

class NoticiaListAPIView(generics.ListAPIView):
    serializer_class = News_Serializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['titulo', 'descricao']
    ordering_fields = ['publicado_em']  # ?ordering=publicado_em ou -publicado_em

    def get_queryset(self):
        qs = News_Informe.objects.all()
        portal = self.request.query_params.get('portal')  # ?portal=cnn

        if portal:
            qs = qs.filter(portal=portal)

        return qs
    

