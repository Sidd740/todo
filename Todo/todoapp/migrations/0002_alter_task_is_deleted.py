# Generated by Django 4.1 on 2022-11-05 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='is_deleted',
            field=models.CharField(default='n', max_length=2),
        ),
    ]