# Generated by Django 4.1 on 2022-09-03 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='ID',
            field=models.CharField(max_length=10),
        ),
    ]
