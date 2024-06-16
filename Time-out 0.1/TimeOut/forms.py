from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets

class FormCadastro(UserCreationForm):
    email = forms.EmailField(label='Email')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {'username': widgets.TextInput(attrs={'class': "form",
                      'placeholder': 'Nome'}),
                  'email': widgets.EmailInput(attrs={'class': "form",
                      'placeholder': 'Exemplo@exe.com'}),
                  'password1': widgets.PasswordInput(attrs={'class': "form",
                      'placeholder': 'Senha'}),
                  'password2': widgets.PasswordInput(attrs={'class': "form",
                      'placeholder': 'Confirme a senha'})}

   
           