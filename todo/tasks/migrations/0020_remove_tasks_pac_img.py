# Generated by Django 3.2.8 on 2022-04-04 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0019_tasks_pac_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='pac_img',
        ),
    ]
