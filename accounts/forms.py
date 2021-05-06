from django import forms
# Modified Sign-Up Form
class InputForm(forms.Form):
    username = forms.CharField(max_length = 200)
    password = forms.CharField(widget = forms.PasswordInput())