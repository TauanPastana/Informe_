from django.db import models

# Create your models here.
class News_Informe(models.Model):
    titulo = models.CharField(max_length=400, blank=False)
    descricao = models.TextField(blank=True)
    imagem = models.URLField(max_length=400, blank=False, null=False)
    publicado_em = models.DateTimeField(null=True, blank=True)
    url = models.URLField(max_length=400, unique=True)
    portal = models.CharField(max_length=20, default="desconhecido")
    

    def __str__(self):
        return self.titulo + f" Portal - {self.portal}"



