from django import forms
from .models import Github


class GithubForm(forms.ModelForm):
    class Meta:
        model = Github
        fields = ['github_username']
