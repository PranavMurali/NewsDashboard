# Generated by Django 3.1.2 on 2020-11-23 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_marks_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
