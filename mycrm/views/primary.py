from functools import wraps
import logging

from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from django.shortcuts import redirect, render
from django.views import generic

from mycrm.forms.forms import LoginForm
from mycrm.models import Record

logger = logging.getLogger(__name__)

class DashboardView(generic.TemplateView):
    abc = 'test'
    template_name = 'mycrm/dashboard.html'

def sign_in(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
            return redirect(request.POST.get('next', ''))
        else:
            msg = 'Error validating the form'    
    else:
        return render(request, "mycrm/accounts/sign-in.html", {"form": form, "msg" : msg})

def sign_up(request):
    return render(request, 'mycrm/sign-up.html')



@login_required(login_url="/mycrm/login")
def dash(request):
    return render(request, 'mycrm/dashboard.html')

@login_required(login_url="/mycrm/login")
def home(request):
    return render(request, 'mycrm/index.html')

@login_required(login_url="/mycrm/login")
def buttons(request):
    return render(request, 'mycrm/volt/ui-buttons.html')

@login_required(login_url="/mycrm/login")
def forms(request):
    return render(request, 'mycrm/volt/ui-forms.html')
    
@login_required(login_url="/mycrm/login")
def modals(request):
    return render(request, 'mycrm/volt/ui-modals.html')

@login_required(login_url="/mycrm/login")
def settings(request):
    return render(request, 'mycrm/volt/settings.html')
    
@login_required(login_url="/mycrm/login")
def bootstrap_tables(request):
    return render(request, 'mycrm/bootstrap-tables.html')