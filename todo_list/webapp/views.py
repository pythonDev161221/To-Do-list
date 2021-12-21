from django.shortcuts import render, redirect

from webapp.models import Task


def task_view(request):
    tasks = Task.objects.all().order_by("date_deadline")
    return render(request, 'index.html', {"tasks": tasks})


def detail_view(request):
    pk = request.GET.get("pk")
    task = Task.objects.get(pk=pk)
    return render(request, 'detail.html', {'task': task})


def delete_view(request):
    pk = request.GET.get("pk")
    task = Task.objects.get(pk=pk)
    task.delete()
    return task_view(request)
