# Generated by Django 4.0.5 on 2022-06-22 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0001_initial'),
        ('authentication', '0004_alter_user_is_active_alter_user_is_staff_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='faculty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='faculty.faculty'),
        ),
    ]