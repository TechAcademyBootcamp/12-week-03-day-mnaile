from django.shortcuts import render
from django.views.generic import ListView
from .models import News
from django.views.generic import DetailView


# Create your views here.

class NewsList(ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = 'news_list'
    
class NewsDetail(DetailView):
    model = News
    template_name = 'post.html'