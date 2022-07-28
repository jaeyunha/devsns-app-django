from django import forms
from .models import Post, Comment, FreePost, FreeComment

class PostForm(forms.ModelForm):
    class Meta:
        mmodel = Post
        fileds = '__all__'
        # fileds = ['title', 'body']
