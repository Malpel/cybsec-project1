# Generated by Django 3.1.2 on 2020-12-21 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badsec_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='balance',
            field=models.IntegerField(default=0),
        ),
    ]