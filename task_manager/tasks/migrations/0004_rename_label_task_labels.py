# Generated by Django 5.0.3 on 2024-04-18 09:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0003_alter_task_executor_alter_task_label"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="label",
            new_name="labels",
        ),
    ]
