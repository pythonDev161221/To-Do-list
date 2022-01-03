from django.shortcuts import render, redirect

from webapp.models import Task


def task_view(request):
    tasks = Task.objects.all().order_by("date_deadline")
    return render(request, 'index.html', {"tasks": tasks})


def detail_view(request, pk):
    task = Task.objects.get(pk=pk)
    return render(request, 'detail.html', {'task': task})


def delete_view(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect("index")


def create_view(request):
    if request.method == 'GET':
        select_status = Task.status_choices
        context = {'selection': select_status}
        return render(request, 'create.html', context)
    else:
        task_text = request.POST.get('task')
        status = request.POST.get('status')
        date_deadline = request.POST.get('date_deadline')
        text = request.POST.get('text')
        task = Task(task=task_text, status=status, date_deadline=date_deadline, text=text)
        task.save()
        return redirect("index")
