# Generated by Django 3.2.3 on 2021-05-24 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
