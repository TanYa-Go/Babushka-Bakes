from django import forms
from django.forms import ModelForm
from .models import Post

class BlogPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'author', 'body', 'image')
        
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control' }),
            'subtitle': forms.TextInput(attrs={'class':'form-control' }),
            'author':forms.Select(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }


class EditPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'body', 'image')
        
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'subtitle': forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }