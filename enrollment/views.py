from django.shortcuts import render, redirect
from django.http import Http404
from django.urls import reverse
from .forms.register_form import RegisterForm

# Create your views here.
def register_view(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)

    return render(
        request,
        'enrollment/pages/register_view.html',{
            "form": form,
        }
    )