# Generated by Django 3.2.8 on 2022-04-04 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0017_alter_tasks_pac_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='pac_img',
        ),
    ]