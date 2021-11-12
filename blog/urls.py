from django.urls import path
from .views import BlogListView, PostDetailView, AddPostView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog'),
    path('post/<int:pk>', PostDetailView.as_view(), name='blog_details'),
    path('add_post/', AddPostView.as_view(), name='add_post'),

]
