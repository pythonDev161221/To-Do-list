from django.urls import path
from .views import task_view, detail_view, delete_view, create_view, update_view

urlpatterns = [
    path('', task_view, name="index"),
    path('task/<int:pk>', detail_view, name="task_detail"),
    path('delete/<int:pk>', delete_view, name="delete"),
    path('create/', create_view, name="task_create"),
    path('update/<int:pk>', update_view, name="task_update"),
]
