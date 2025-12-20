from rest_framework import serializers
from .models import News_Informe


class News_Serializer(serializers.ModelSerializer):

    class Meta:
        verbose_name_plural = "Informe"
        model = News_Informe
        fields = '__all__'