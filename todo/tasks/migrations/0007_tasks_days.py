# Generated by Django 3.2.8 on 2022-03-31 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_auto_20220331_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='days',
            field=models.CharField(default='', max_length=2),
        ),
    ]