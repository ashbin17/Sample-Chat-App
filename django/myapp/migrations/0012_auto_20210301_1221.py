# Generated by Django 3.1.5 on 2021-03-01 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_customuser_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='pic',
            field=models.CharField(max_length=100),
        ),
    ]