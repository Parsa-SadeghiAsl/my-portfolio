from django import forms
from django.forms import TextInput, EmailInput, Textarea
from .models import Comment


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        # Custom logic for initializing the form
        self.fields['name'].label = ''
        self.fields['email'].label = ''
        self.fields['body'].label = ''
        
        
    class Meta:
        model = Comment
        fields = ("name", "email", "body")
        widgets = {
            'name': TextInput(attrs={'class':'comment_name mt-3 ', 'placeholder': 'Name'}),
            'email': EmailInput(attrs={'class':'comment_email mt-3', 'placeholder': 'Email'}),
           'body': Textarea(attrs={'class':'comment_body mt-3', 'rows':5, 'cols':30})
        }