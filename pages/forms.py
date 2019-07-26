from django import forms
from .models import Comment, Query

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

