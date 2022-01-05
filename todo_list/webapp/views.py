from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound
from django.urls import reverse

from webapp.models import Task, STATUS_CHOICES


def task_view(request):
    tasks = Task.objects.all().order_by("date_deadline")
    return render(request, 'index.html', {"tasks": tasks})


def detail_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'detail.html', {'task': task})


def delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect("index")


def create_view(request):
    if request.method == 'GET':
        select_status = STATUS_CHOICES
        context = {'selection': select_status}
        return render(request, 'create.html', context)
    else:
        task_text = request.POST.get('task')
        status = request.POST.get('status')
        date_deadline = request.POST.get('date_deadline')
        if not date_deadline:
            return HttpResponseNotFound("date mistake has been occurred, it is need to input date")
        description = request.POST.get('description')
        task = Task(task=task_text, status=status, date_deadline=date_deadline, description=description)
        task.save()
        return redirect("index")

