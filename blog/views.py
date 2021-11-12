from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import BlogPostForm
# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'blog.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog_details.html' 
    

class AddPostView(CreateView):
    model = Post
    form_class = BlogPostForm
    template_name = 'add_blog_post.html'
    