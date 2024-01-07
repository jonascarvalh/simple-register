from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # enroll type create later
        # extern
        # employee
        # student (matricula no SIGUEMA)
        # teacher (matricula no SIGUEMA)

    first_name = forms.CharField(
        error_messages={'required': 'Escreva o seu primeiro nome'},
        required=True,
        label='Primeiro Nome'
    )

    last_name = forms.CharField(
        error_messages={'required': 'Escreva o seu sobrenome'},
        required=True,
        label='Sobrenome'
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
            'first_name',
            'last_name',
            'email',
            'password',
            'password2',
        ]