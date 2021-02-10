from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
# Create your views here.


class BlogView(ListView):
    model = Post
    context_object_name = 'all_blog_objects'
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'detay.html'


class BlogCreateNew(CreateView):
    model = Post
    template_name = 'post_yeni.html'
    # bu kisim onemli modelde olusturulan butun kisimlari aliyoruz.
    fields = "__all__"


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body', ]


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    # reverseun tersi olarak kullandik, BlogDeleteView islemi bitene kadar url yonledinrmesi yapmiyacak.
    success_url = reverse_lazy('anasayfa')
