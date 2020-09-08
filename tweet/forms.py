from django import forms
from tweet.models import Tweet
from django.forms import Textarea


class MakeTweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ["tweet"]
        widgets = {
            'tweet': Textarea(attrs={'onkeyup':"countChar(this)"})
        }
