from django.contrib import admin
from .models import Record

class RecordAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['created_by']}),
    ]
    list_display = ('created_by', 'created_at')

admin.site.register(Record, RecordAdmin)
# Register your models here.
