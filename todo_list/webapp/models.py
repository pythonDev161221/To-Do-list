from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name="Заголовок")
    status = models.CharField(max_length=200, null=False, blank=False, verbose_name="Статус", default="new")
    date_done = models.DateField(null=True, blank=True, default=None)

