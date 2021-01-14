# Generated by Django 3.0.4 on 2020-11-23 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cciit', '0003_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cabinet_name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, verbose_name='Название кабинета')),
            ],
            options={
                'verbose_name': 'Название кабинета',
                'verbose_name_plural': 'Название кабинета',
            },
        ),
    ]