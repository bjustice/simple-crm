from functools import wraps
import logging
import json
from django.contrib.auth.models import Group

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
        custom_field_count = request.POST.get('custom_field_count')
        form = AddRecordGroupForm(request.POST, custom_fields=custom_field_count)
        print(form.is_valid())
        print(form)
        if form.is_valid():
            print(form.cleaned_data)

            fields = []
            for i in range(0, int(custom_field_count)):
                field_name = 'custom_field_' + str(i)
                fields.append(form.cleaned_data[field_name])
            fieldDefs = __format_field_defs__(fields)

            record_group = RecordGroup(
                group_name=form.cleaned_data['group_name'],
                company_id=form.cleaned_data['company'],
                field_definitions=fieldDefs,
            )
            record_group.save()
            data['status'] = 'Successly added record.'
        else:
            data['status'] = 'Unable to add record'
    return render(request,'mycrm/record_type/add.html', data)


def __format_field_defs__(fields):
    fieldDefs=  {}
    
    for index, field in enumerate(fields):
        fieldDefs[str(index)] = field

    print(fieldDefs)
    return fieldDefs