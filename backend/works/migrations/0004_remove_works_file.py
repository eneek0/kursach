# Generated by Django 4.0.5 on 2022-07-10 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0003_remove_works_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='works',
            name='file',
        ),
    ]
