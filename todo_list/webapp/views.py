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


def create_view(request):
    if request.method == 'GET':
        select_status = Task.status_choices
        # print(select_status)
        # context = {}
        # for i in select_status:
        #     context[i[0]] = i[1]
        # print(context)
        context = {'selection': select_status}
        return render(request, 'create.html', context)
