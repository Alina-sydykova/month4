from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField()
    password_confirm = forms.CharField()

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)