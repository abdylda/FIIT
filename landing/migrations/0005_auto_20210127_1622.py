# Generated by Django 3.0.4 on 2021-01-27 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0004_auto_20210127_1618'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='documents',
            options={'verbose_name': 'Документы', 'verbose_name_plural': 'Документы'},
        ),
        migrations.AlterField(
            model_name='documents',
            name='file',
            field=models.FileField(blank=True, upload_to='Документы'),
        ),
    ]
