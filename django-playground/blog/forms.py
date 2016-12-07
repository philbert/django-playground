""" django forms for comments """
from django import forms

from blog.models import Comment

class CommentForm(forms.ModelForm):
    """ class docstring """
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

    def __init__(self, *args, **kwargs):
        self.entry = kwargs.pop('entry')    # the blog entry instance
        super().__init__(*args, **kwargs)

    def save(self):
        """ overridden save method """
        comment = super().save(commit=False)
        comment.entry = self.entry
        comment.save()
        return comment
