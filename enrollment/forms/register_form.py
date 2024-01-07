from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    name = forms.CharField(
        error_messages={'required': 'Escreva o seu primeiro nome'},
        required=True,
        label='Primeiro Nome'
    )

    email = forms.EmailField(
        error_messages={'required': 'O e-mail é orbigatório'},
        required=True,
        label='E-mail'
    )

    password = forms.CharField(
        error_messages={'required': 'A senha não pode ser vazia'},
        widget=forms.PasswordInput(),
        required=True,
        label='Senha'
    )

    password2 = forms.CharField(
        error_messages={'required': 'A senha não pode ser vazia'},
        widget=forms.PasswordInput(),
        required=True,
        label='Confirme sua senha'
    )

    # create enroll_type later
    
    class Meta:
        model = User
        fields = [
            'name',
            'email',
            'password',
            'password2',
        ]