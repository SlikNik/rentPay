from django import forms
from customUsers.models import MyUser



class SignupForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ['firstname', 'lastname', 'age', 'displayname', 'street', 'apt', 'city', 'state']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)
