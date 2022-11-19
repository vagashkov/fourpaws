from django.urls import path

from .views import BlogListView, BlogDetailsView, BlogCreateView, BlogEditView, BlogDeleteView, AboutPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', BlogEditView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', BlogDetailsView.as_view(), name='post_details'),
    path('', BlogListView.as_view(), name='post_list'),
]