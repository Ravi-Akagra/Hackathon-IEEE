# Generated by Django 4.1.1 on 2022-10-01 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0004_remove_student_gender_student_city"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="parents_Or_Guardian",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name="student",
            name="state",
            field=models.CharField(blank=True, max_length=200),
        ),
    ]