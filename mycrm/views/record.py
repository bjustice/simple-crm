import logging

from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from mycrm.forms.forms import AddRecordForm, UpdateRecordForm
from mycrm.models import Record

logger = logging.getLogger(__name__)

@login_required(login_url="/mycrm/login")
def post_record(request):
    if request.method == 'POST':
        form = AddRecordForm(request.POST)
        if form.is_valid():
            record = Record(first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'])
            record.save()
            
            return render(request, 'mycrm/record/add.html', { 'status': 'Successly added record.' })
        return render(request, 'mycrm/record/add.html', { 'status': form })
    else:
        return render(request, 'mycrm/record/add.html')

@login_required(login_url="/mycrm/login")
def summary(request):
    records = Record.objects.all()
    return render(request, 'mycrm/record/summary.html', { 'records': records })

@login_required(login_url="/mycrm/login")
def detail(request, record_id):
    if request.method == 'POST':
        
        form = UpdateRecordForm(request.POST)
        record = Record.objects.get(id=record_id)
        if form.is_valid():
            record.first_name = form.cleaned_data['first_name']
            record.last_name = form.cleaned_data['last_name']
            record.save()
            return render(request, 'mycrm/record/detail.html', { 'record': record })
        return render(request, 'mycrm/record/detail.html', { 'record': record })

    record = get_object_or_404(Record, pk=record_id)

    return render(request, 'mycrm/record/detail.html', { 'record': record })
