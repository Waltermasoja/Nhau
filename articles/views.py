from django.shortcuts import render
from django.views.generic import (
    ListView,
    DeleteView,
    DetailView,
    UpdateView,
    CreateView
    )
from .models import article
from django.urls import reverse_lazy

class ArticleListView(ListView):
    model = article
    template_name = 'article_list.html'

class ArticleDetailView(DetailView):
    model = article
    template_name = 'article_detail.html' 

class ArticleUpdateView(UpdateView) :
    model = article
    fields = ['title','body']
    template_name = 'article_update.html'  

class ArticleDeleteView(DeleteView):
    model = article
    template_name  = 'article_delete.html'
    success_url = reverse_lazy('article_list')

class ArticleCreateView(CreateView): 
    model = article
    fields = ['title','body','author']
    template_name = 'article_new.html'
   



