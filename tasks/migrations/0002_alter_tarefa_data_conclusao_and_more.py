# Generated by Django 4.2.3 on 2023-07-31 00:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tarefa",
            name="data_conclusao",
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name="tarefa",
            name="data_criacao",
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name="tarefa",
            name="data_prazo",
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]