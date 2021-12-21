from django.db import models

# Create your models here.


class Task(models.Model):
    task = models.CharField(max_length=200, null=False, blank=False, verbose_name="Заголовок")
    status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]
    status = models.CharField(max_length=200, null=False, blank=False, choices=status_choices, verbose_name="Статус", default="new")
    date_deadline = models.DateField(null=True, blank=True, default=None)

