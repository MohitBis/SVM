# Generated by Django 2.2.5 on 2020-05-18 09:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20200518_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='sanskritammember',
            name='course',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]
