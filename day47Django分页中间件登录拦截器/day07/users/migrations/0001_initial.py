# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-18 09:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, unique=True, verbose_name='姓名')),
                ('password', models.CharField(max_length=255, verbose_name='密码')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建是时间')),
                ('operate_time', models.DateTimeField(auto_now_add=True, verbose_name='修改时间')),
                ('icon', models.ImageField(null=True, upload_to='upload')),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='UserTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket', models.CharField(max_length=30)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建是时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Users')),
            ],
            options={
                'db_table': 'user_ticekt',
            },
        ),
    ]
