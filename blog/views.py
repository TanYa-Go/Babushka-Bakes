from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from .models import Post
from .forms import BlogPostForm, EditPostForm

# Create your views here.


class BlogListView(ListView):
    """
    View that renders all blog posts
    """
    model = Post
    template_name = 'blog.html'
    ordering = ['-id']


class PostDetailView(DetailView):
    """
    View that renders blog post details
    """
    model = Post
    template_name = 'blog_details.html'


class AddPostView(CreateView):
    """
    Lets superuser to add a blog post
    """
    model = Post
    form_class = BlogPostForm
    template_name = 'add_blog_post.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return HttpResponseRedirect(reverse('blog'))


class UpdatePostView(UpdateView):
    """
    Lets superuser to edit blog posts
    """
    model = Post
    form_class = EditPostForm
    template_name = 'edit_blog_post.html'
    success_url = reverse_lazy('blog')


class DeletePostView(DeleteView):
    """
    Lets superuser to delete blog posts
    """
    model = Post
    template_name = 'delete_blog_post.html'
    success_url = reverse_lazy('blog')
