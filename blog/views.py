from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Post
from .forms import BlogPostForm, EditPostForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
# Create your views here.


class BlogListView(ListView):
    model = Post
    template_name = 'blog.html'
    ordering = ['-id']


class PostDetailView(DetailView):
    """r"""
    model = Post
    template_name = 'blog_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = BlogPostForm
    template_name = 'add_blog_post.html'
    
    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return HttpResponseRedirect(reverse('blog'))


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'edit_blog_post.html'
    success_url = reverse_lazy('blog')


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_blog_post.html'
    success_url = reverse_lazy('blog')
