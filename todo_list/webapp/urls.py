from django.urls import path
from .views import task_view, detail_view, delete_view, create_view

urlpatterns = [
    path('', task_view, name="index"),
    path('task/', detail_view),
    path('delete/<int:pk>', delete_view, name="delete"),
    path('create/', create_view),
]
