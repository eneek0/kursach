# Generated by Django 4.0.5 on 2022-07-06 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('achievements', '0001_initial'),
        ('authentication', '0005_user_faculty'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='achievements',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='achievements.achievements'),
        ),
    ]