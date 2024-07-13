# Generated by Django 5.0 on 2023-12-29 10:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dolzn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должности',
            },
        ),
        migrations.CreateModel(
            name='WebSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Вэб-система',
                'verbose_name_plural': 'Вэб-системы',
            },
        ),
        migrations.CreateModel(
            name='AdvUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя пользователя')),
                ('dolzn', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.dolzn', verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Protocol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('time', models.IntegerField(verbose_name='Время в минутах')),
                ('traffic', models.IntegerField(verbose_name='Трафик')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.advuser', verbose_name='Пользователь')),
                ('websystem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.websystem', verbose_name='Система')),
            ],
        ),
    ]
