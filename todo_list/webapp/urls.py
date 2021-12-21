from django.urls import path
from .views import task_view, detail_view

urlpatterns = [
    path('', task_view),
    path('task/', detail_view)
]
