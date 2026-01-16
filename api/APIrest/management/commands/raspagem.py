from django.core.management.base import BaseCommand

from ...models import News_Informe
from src.classes.G1 import noticias_G1
from src.classes.cnn import noticias_CNN
from src.classes.metropole import noticiasMetropoles

from django.db import DataError


    



class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            for dados in noticias_G1() + noticias_CNN() + noticiasMetropoles():
                News_Informe.objects.update_or_create(
                    url=dados["url"],
                    defaults=dados,
                )
        
        except DataError as e:
            print("ERRO AO SALVAR ESSE REGISTRO:")
            print("titulo len:", len(dados.get("titulo", "")))
            print("url len:", len(dados.get("url", "")))
            print("imagem len:", len(dados.get("imagem", "")))
            print("portal len:", len(dados.get("portal", "")))
            print("dados completos:", dados)
            raise

    