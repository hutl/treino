from django.db import models

class Produto(models.Model):
    nome_prod = models.CharField(max_length=150)
    descrição = models.TextField(max_length=1000, default="")
    preço = models.DecimalField(max_digits=7, decimal_places=2, default= 0)
    qtd = models.PositiveIntegerField()
    imagem = models.ImageField(upload_to='uploads/',default="")