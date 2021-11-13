from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import BlogPostForm, EditPostForm
from django.urls import reverse_lazy
# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'blog.html'
    ordering = ['-id']


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog_details.html' 
    

class AddPostView(CreateView):
    model = Post
    form_class = BlogPostForm
    template_name = 'add_blog_post.html'
    

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'edit_blog_post.html'
    # fields = ['title', 'body', 'image']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_blog_post.html'
    success_url = reverse_lazy('blog')