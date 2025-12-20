from ...models import News_Informe
from src.classes.G1 import noticias_G1
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        lista_de_dicts = noticias_G1()
        for dados in lista_de_dicts:
            News_Informe.objects.update_or_create(
                url=dados["url"],
                defaults=dados,
            )
    