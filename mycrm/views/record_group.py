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
    
    data = { 'companies': Company.objects.all(), 'extra_field_count': 0 }
    if request.method == 'POST':
        form = AddRecordGroupForm(request.POST)
        print(form)
        if form.is_valid():
            record_group = RecordGroup(
                group_name=form.cleaned_data['group_name'],
                company_id=form.cleaned_data['company'],
                number_of_fields=form.cleaned_data['number_of_fields'],
                custom_fields=form.cleaned_data['custom_field_count']
            )
            record_group.save()
            data['status'] = 'Successly added record.'
        data['status'] = 'Unable to add record'
    return render(request,'mycrm/record_type/add.html', data)

def myview(request):
    print(request.POST)
    if request.method == 'POST':
        print("COUNT!!!" + request.POST.get('extra_field_count'))
        # form = MyForm(request.POST, extra=request.POST.get('extra_field_count'))
        if form.is_valid():
            print("valid!")
    else:
        form = MyForm()
    return render(request, "mycrm/record_type/example.html", { 'form': form })