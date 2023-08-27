from django.db import models

class Produto(models.Model):
    nome_prod = models.CharField(max_length=150)
    descricao = models.TextField(max_length=500, default="")
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    qtd = models.IntegerField()
    imagem = models.ImageField(upload_to='uploads/',default="")