from rest_framework.views import APIView
from rest_framework.response import Response
from .models import News_Informe
from .serializer import News_Serializer

class News_APIview(APIView):

    def get(self, request):
        news = News_Informe.objects.all()
        serializer = News_Serializer(news, many=True)
        return Response(serializer.data)
    

