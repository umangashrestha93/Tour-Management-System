# Generated by Django 3.2.8 on 2022-04-04 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0012_alter_tasks_pac_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='pac_img',
            field=models.ImageField(null=True, upload_to='pac_images/'),
        ),
    ]
