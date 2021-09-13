from functools import wraps
import logging

from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect, render
from django.views import generic

from mycrm.forms.record_group import AddRecordGroupForm
from mycrm.models import Company, RecordGroup

logger = logging.getLogger(__name__)


@login_required(login_url="/mycrm/login")
def post_record_group(request):
    
    data = { 'companies': Company.objects.all(), }
    if request.method == 'POST':
        form = AddRecordGroupForm(request.POST)
        print(form)
        if form.is_valid():
            print(form.cleaned_data)
            record_group = RecordGroup(group_name=form.cleaned_data['group_name'], company_id=form.cleaned_data['company'])
            record_group.save()
            data['status'] = 'Successly added record.'
        data['status'] = 'Unable to add record'
    return render(request,'mycrm/record_type/add.html', data)
