from django.urls import path
from .views import News_APIview

urlpatterns = [
    path('informe', view=News_APIview.as_view())
]