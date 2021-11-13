from django import forms
from django.forms import ModelForm
from .models import Post

class BlogPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'body', 'image')
        
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Post Title'}),
            'author':forms.Select(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control','placeholder': 'Your text here...'}),
        }


class EditPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'image')
        
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Post Title'}),
            'body':forms.Textarea(attrs={'class':'form-control','placeholder': 'Your text here...'}),
        }