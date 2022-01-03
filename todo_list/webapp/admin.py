from django.contrib import admin

from webapp.models import Task


# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ['pk', 'task', 'status', 'date_deadline']
    list_filter = ['status']
    search_fields = ['task', 'status']
    fields = ['task', 'status', 'date_deadline', 'text']


admin.site.register(Task, TaskAdmin)
