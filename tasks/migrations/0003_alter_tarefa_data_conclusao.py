# Generated by Django 4.2.3 on 2023-07-31 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0002_alter_tarefa_data_conclusao_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tarefa",
            name="data_conclusao",
            field=models.DateField(blank=True),
        ),
    ]
