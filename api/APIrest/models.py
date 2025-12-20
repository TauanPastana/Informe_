from django.db import models

# Create your models here.
class News_Informe(models.Model):
    titulo = models.CharField(max_length=100, blank=False)
    descricao = models.TextField(blank=True)
    imagem = models.URLField(blank=False, null=False)
    publicado_em = models.DateTimeField(null=True, blank=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.url



