from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from .models import *

class IndexView (ListView):
   model = Produto
   template_name= "index.html"
   context_object_name = 'produtos'

class ProdutoView(DetailView):
    model = Produto
    template_name = "produto.html"
   
    def post(self, request, *args, **kwargs):
        produto = self.get_object()
        produto.qtd -= 1
        produto.save()
        return redirect('index')