from .models import SignUp
from django import forms


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['username','email']

class EmailForm(forms.Form):
    # tester si ca marche email field
    # add a comment test
    email = forms.EmailField()
    username = forms.CharField(max_length=254)
