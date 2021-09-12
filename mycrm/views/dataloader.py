from functools import wraps
import logging

from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect, render
from django.views import generic

logger = logging.getLogger(__name__)

@login_required(login_url="/mycrm/login")
def data_loader(request):
    return render(request, 'mycrm/dataloader/load.html')
