from functools import wraps
import logging

from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from ..forms import LoginForm, SignUpForm
from ..models import Choice, Question, Record

logger = logging.getLogger(__name__)

class IndexView(generic.ListView):
    template_name = 'mycrm/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'mycrm/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'mycrm/results.html'

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
        logger.warning("not post")
        return render(request, "mycrm/sign-in.html", {"form": form, "msg" : msg})

def sign_up(request):
    return render(request, 'mycrm/sign-up.html')

@login_required(login_url="/mycrm/login")
def home(request):
    return render(request, 'mycrm/index.html')

@login_required(login_url="/mycrm/login")
def buttons(request):
    return render(request, 'mycrm/ui-buttons.html')

@login_required(login_url="/mycrm/login")
def settings(request):
    return render(request, 'mycrm/settings.html')
    
@login_required(login_url="/mycrm/login")
def forms(request):
    return render(request, 'mycrm/ui-forms.html')

@login_required(login_url="/mycrm/login")
def dash(request):
    return render(request, 'mycrm/dashboard.html')

def bootstrap_tables(request):
    return render(request, 'mycrm/bootstrap-tables.html')