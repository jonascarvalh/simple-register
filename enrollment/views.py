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
            "form_action": reverse('enrollment:register_create')
        }
    )

def register_create(request):
    if not request.POST:
        raise Http404()
    
    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()

        del(request.session['register_form_data'])
        return redirect(reverse('enrollment:login'))
    
    return redirect(reverse('enrollment:registro'))

