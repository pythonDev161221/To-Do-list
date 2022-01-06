from django import forms
from django.forms import SelectDateWidget, widgets

from .models import STATUS_CHOICES


class TaskForm(forms.Form):
    task = forms.CharField(max_length=200, required=True, label="Task")
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=True, label="Status", initial=STATUS_CHOICES[0][1])
    description = forms.CharField(max_length=2000, required=False, label="Description", widget=forms.Textarea)
    date_deadline = forms.DateField(label="Дата публикации",
                                       widget=widgets.DateTimeInput(attrs={"type": "date"}),
                                       required=True)
