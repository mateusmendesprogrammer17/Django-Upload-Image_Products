from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=100, null=False)
    categoria = models.CharField(max_length=100)
    preco = models.FloatField(null=False)
    imagem = models.ImageField(upload_to='store/imagens', null=True)
    quantidade = models.IntegerField()
    def __str__(self):
        return self.nome