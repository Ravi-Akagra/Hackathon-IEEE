# Generated by Django 4.1.1 on 2022-10-01 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0005_student_parents_or_guardian_student_state"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="current_status",
        ),
    ]
