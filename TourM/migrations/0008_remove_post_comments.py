# Generated by Django 4.0.3 on 2022-04-18 02:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TourM', '0007_post_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comments',
        ),
    ]
