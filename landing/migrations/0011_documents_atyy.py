# Generated by Django 3.0.4 on 2021-01-27 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0010_auto_20210127_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='documents',
            name='atyy',
            field=models.CharField(default=2, max_length=100, verbose_name='Аты'),
            preserve_default=False,
        ),
    ]