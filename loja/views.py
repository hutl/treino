from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

class Index (ListView):
   model = Produto
   template_name= "index.html"
   context_object_name = 'produtos'

