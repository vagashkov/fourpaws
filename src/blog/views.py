from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post


# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'blogs/home.html'
    context_object_name = 'all_posts'


class BlogDetailsView(DetailView):
    model = Post
    template_name = 'blogs/details.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'blogs/create.html'
    fields = ['title', 'author', 'text']


class BlogEditView(UpdateView):
    model = Post
    template_name = 'blogs/edit.html'
    fields = ['title', 'text']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blogs/delete.html'
    success_url = reverse_lazy('post_list')


class AboutPageView(TemplateView):
    template_name = 'blogs/about.html'
