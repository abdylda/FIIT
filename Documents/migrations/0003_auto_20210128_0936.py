# Generated by Django 3.0.4 on 2021-01-28 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Documents', '0002_auto_20210127_1931'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='atyy',
        ),
        migrations.AddField(
            model_name='document',
            name='name',
            field=models.CharField(default=2, max_length=100, verbose_name='Название документ '),
            preserve_default=False,
        ),
    ]
