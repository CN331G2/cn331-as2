# Generated by Django 4.1 on 2022-08-30 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=64)),
                ('semester', models.CharField(max_length=1)),
                ('year', models.IntegerField()),
                ('seat', models.IntegerField()),
                ('quota', models.IntegerField(default=False)),
            ],
        ),
    ]