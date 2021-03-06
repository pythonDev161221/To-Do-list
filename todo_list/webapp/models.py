from django.db import models

# Create your models here.
STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


class Task(models.Model):
    task = models.CharField(max_length=200, null=False, blank=False, verbose_name="Заголовок")
    status = models.CharField(max_length=200, null=False, blank=False, choices=STATUS_CHOICES, verbose_name="Статус",
                              default="new")
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name="Описание")
    date_deadline = models.DateField(null=True, blank=True, default=None)

    def __str__(self):
        return "{}. {}".format(self.pk, self.task)

    class Meta:
        ordering = ['date_deadline']
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
