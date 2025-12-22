from django.core.management.base import BaseCommand

from ...models import News_Informe
from src.classes.G1 import noticias_G1
from src.classes.cnn import noticias_CNN


class Command(BaseCommand):
    def handle(self, *args, **options):
        for dados in noticias_G1() + noticias_CNN():
            News_Informe.objects.update_or_create(
                url=dados["url"],
                defaults=dados,
            )

    