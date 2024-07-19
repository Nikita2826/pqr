from django import forms
from .models import Post

class PostForm(forms.Form):
    id = forms.IntegerField()
    title = forms.CharField(max_length=200)
    content = forms.TextInput()
    create_at = forms.DateInput()
    update_at =forms.DateInput()