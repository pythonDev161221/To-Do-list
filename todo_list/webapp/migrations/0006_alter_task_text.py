# Generated by Django 4.0 on 2022-01-03 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_alter_task_options_task_text_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='text',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='Описание'),
        ),
    ]
