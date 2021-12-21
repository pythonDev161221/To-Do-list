from django.shortcuts import render

from webapp.models import Task


def task_view(request):
    tasks = Task.objects.all().order_by("date_deadline")
    return render(request, 'index.html', {"tasks": tasks})


def detail_view(request):
    if request.method == "GET":
        pk = request.GET.get("pk")
        task = Task.objects.get(pk=pk)
        return render(request, 'detail.html', {'task': task})
    elif request.method == "POST":
        # print('asdfasdfasdf')
        # pk = request.POST.get("pk")

        # task = Task.objects.get(pk=pk)
        # task.delete()
        return render(request, 'index.html')
