from django import forms
from twitteruser.models import TwitterUser


class SignupForm(forms.Form):
    username = forms.CharField(max_length=80)
    password = forms.CharField(widget=forms.PasswordInput)
