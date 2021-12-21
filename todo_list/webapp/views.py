from django.shortcuts import render


# Create your views here.
from webapp.models import Task


def task_view(request):
    tasks = Task.objects.all().order_by("date_deadline")
    return render(request, 'index.html', {"tasks": tasks})
