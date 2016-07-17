from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from PI.models import Kiply


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    kiply_key = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", 'kiply_key', 'email')

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            kiply = Kiply()
            kiply.user = user
            kiply.save()
        return user