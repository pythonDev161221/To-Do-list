from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound
from django.urls import reverse

from webapp.forms import TaskForm
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
        form = TaskForm()
        # select_status = STATUS_CHOICES
        # context = {'selection': select_status}
        # return render(request, 'create.html', context)
        return render(request, 'create.html', {'form': form})
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task_text = request.POST.get('task')
            status = request.POST.get('status')
            print(request.POST.get('date_deadline'))
            date_deadline = request.POST.get('date_deadline')
            description = request.POST.get('description')
            task = Task(task=task_text, status=status, date_deadline=date_deadline, description=description)
            task.save()
            return redirect("index")
        return render(request, "create.html", {'form': form})
        # if not date_deadline:
        #     return HttpResponseNotFound("date mistake has been occurred, it is need to input date")


def update_view(request, pk):
    print(pk)
    print(request)
    task = get_object_or_404(Task, pk=pk)
    if request.method == "GET":
        form = TaskForm(initial={
            'task': task.task,
            'status': task.status,
            'description': task.description,
            'date_deadline': task.date_deadline,
        })
        return render(request, "update.html", {"task": task, "form": form})
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid:
            task.task = request.POST.get('task')
            task.status = request.POST.get('status')
            task.description = request.POST.get('description')
            task.date_deadline = request.POST.get('date_deadline')
            return redirect("task_detail", pk=task.pk)
        return render(request, "update.html", {"task": task, "form": form})

