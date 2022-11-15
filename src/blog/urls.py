from django.urls import path

from .views import BlogListView, BlogDetailsView, AboutPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('post/<int:pk>/', BlogDetailsView.as_view(), name='post_details'),
    path('', BlogListView.as_view(), name='post_list'),
]