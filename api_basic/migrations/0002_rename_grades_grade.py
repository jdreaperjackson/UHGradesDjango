# Generated by Django 3.2.7 on 2021-09-05 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Grades',
            new_name='Grade',
        ),
    ]