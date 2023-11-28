from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    def __init__(self, *args, ***kawargs):
        super().__init__(*args, **kwargs)

    # username
    # first name
    # last name
    # email
    # number
    # user type
        # extern
        # employee
        # student (matricula no SIGUEMA)
        # teacher (matricula no SIGUEMA)