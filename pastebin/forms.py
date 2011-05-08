from django import forms
from django.forms import ModelForm
from paest.pastebin.models import Snippet

class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        fields = ('code', 'lexer', 'expires_options', 'locked')
