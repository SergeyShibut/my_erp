# Generated by Django 4.0.4 on 2022-05-29 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirements',
            name='text',
            field=models.CharField(blank=True, max_length=250, verbose_name='Тех. требования кратко'),
        ),
    ]