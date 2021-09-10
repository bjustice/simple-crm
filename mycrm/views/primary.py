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

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'mycrm/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('mycrm:results', args=(question.id,)))

def sign_in(request):

    form = LoginForm(request.POST or None)
    msg = None
    if request.method == "POST":
        if form.is_valid():
            session['logged_in'] = True
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            print(request.POST)
            return redirect(request.POST.get('next', ''))
        else:
            msg = 'Error validating the form'    
    else:
        logger.warning("not post")
        return render(request, "working/sign-in.html", {"form": form, "msg" : msg})

def sign_up(request):
    return render(request, 'working/sign-up.html')

@login_required(login_url="/mycrm/login")
def home(request):
    return render(request, 'working/index.html')


def dashboard(request):
    return render(request, 'working/dashboard.html')

@login_required(login_url="/mycrm/login")
def dash(request):
    return render(request, 'mycrm/dashboard.html')

def bootstrap_tables(request):
    return render(request, 'working/bootstrap-tables.html')