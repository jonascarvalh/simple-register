from django.shortcuts import render, redirect
from django.http import Http404
from django.urls import reverse

# Create your views here.
def register_view(request):
    return render(
        request,
        'enrollment/pages/register_view.html'
    )