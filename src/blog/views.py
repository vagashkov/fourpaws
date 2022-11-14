from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Post


# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = 'blogs/home.html'
    context_object_name = 'all_posts'


class AboutPageView(TemplateView):
    template_name = 'blogs/about.html'
