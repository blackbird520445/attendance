# Generated by Django 5.0.6 on 2024-05-16 19:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_studentit_studentattendanceit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentattendanceit',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.studentit'),
        ),
    ]
