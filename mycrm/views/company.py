from functools import wraps
import logging

from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect, render
from django.views import generic

from mycrm.models import Company
from mycrm.forms.company import AddCompanyForm

logger = logging.getLogger(__name__)

@login_required(login_url="/mycrm/login")
def post_company(request):
    if request.method == 'POST':
        form = AddCompanyForm(request.POST)
        if form.is_valid():
            company = Company(company_name=form.cleaned_data['company_name'])
            company.save()
            
            return render(request, 'mycrm/company/add.html', { 'status': 'Successly added record.' })
        return render(request, 'mycrm/company/add.html', { 'status': form })
    else:
        return render(request, 'mycrm/company/add.html')
