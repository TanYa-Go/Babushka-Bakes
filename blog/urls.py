from django.urls import path
from .views import (BlogListView, PostDetailView,
                    AddPostView, UpdatePostView, DeletePostView)


urlpatterns = [
    path('', BlogListView.as_view(), name='blog'),
    path('post/<int:pk>', PostDetailView.as_view(), name='blog_details'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name='edit_post'),
    path('post/delete/<int:pk>', DeletePostView.as_view(), name='delete_post'),
]
