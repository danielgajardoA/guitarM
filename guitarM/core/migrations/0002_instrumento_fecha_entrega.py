# Generated by Django 3.0.8 on 2020-07-26 17:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrumento',
            name='fecha_entrega',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
