from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import Post


# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'blogs/home.html'
    context_object_name = 'all_posts'


class BlogDetailsView(DetailView):
    model = Post
    template_name = 'blogs/details.html'


class AboutPageView(TemplateView):
    template_name = 'blogs/about.html'
