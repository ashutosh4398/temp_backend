# Generated by Django 3.2.3 on 2021-05-24 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_lead',
            field=models.BooleanField(default=False),
        ),
    ]