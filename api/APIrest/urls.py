from django.urls import path
from .views import News_APIview_all, News_Apiview_cnn, News_Apiview_g1

urlpatterns = [
    path('informe-all', view=News_APIview_all.as_view()),
    path('informe-cnn', view=News_Apiview_cnn.as_view()),
    path('informe-g1', view= News_Apiview_g1.as_view())
    
]