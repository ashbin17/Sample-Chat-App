# Generated by Django 3.1.5 on 2021-02-28 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_customuser_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='pic',
        ),
    ]
