from .models import SignUp
from django import forms


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['username','email']


# Second way to build a form :
class EmailForm(forms.Form):
    email = forms.EmailField()
    username = forms.CharField(max_length=254)
