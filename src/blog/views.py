from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blogs/create.html'
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blogs/edit.html'
    fields = ['title', 'text']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blogs/delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user



class AboutPageView(TemplateView):
    template_name = 'blogs/about.html'
