import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.db.models import JSONField

class Base(models.Model):
    created_by = models.CharField(max_length=200, default="admin")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=200, default="admin")
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Company(Base):
    company_name = models.CharField(max_length=50)
    def __str__(self):
        return self.id

class RecordGroup(Base):
    group_name = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    numberOfFields = models.IntegerField(default=0)
    field_definitions = JSONField(default=dict)
    def __str__(self):
        return self.id

class Record(Base):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    record_group = models.ForeignKey(RecordGroup, on_delete=models.CASCADE)
    def __str__(self):
        return self.id