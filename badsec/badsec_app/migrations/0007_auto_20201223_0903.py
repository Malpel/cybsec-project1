# Generated by Django 3.1.2 on 2020-12-23 09:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('badsec_app', '0006_auto_20201223_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Client',
        ),
    ]
