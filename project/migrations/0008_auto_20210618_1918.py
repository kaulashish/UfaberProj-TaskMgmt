# Generated by Django 3.2.4 on 2021-06-18 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0007_auto_20210618_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assigned_to',
            field=models.ManyToManyField(help_text='Assignees for task', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(help_text='Project of task', on_delete=django.db.models.deletion.CASCADE, to='project.project'),
        ),
        migrations.CreateModel(
            name='SubTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of subtask', max_length=255)),
                ('description', models.TextField(help_text='Description of subtask')),
                ('start_date', models.DateField(help_text='Start date for subtask', null=True)),
                ('end_date', models.DateField(help_text='Deadline for subtask', null=True)),
                ('assigned_to', models.ManyToManyField(help_text='Assignees for subtask', to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(help_text='Task of task', on_delete=django.db.models.deletion.CASCADE, to='project.task')),
            ],
        ),
    ]
