# Generated by Django 4.1 on 2022-09-14 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_quota'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='code',
        ),
        migrations.RemoveField(
            model_name='course',
            name='name',
        ),
        migrations.RemoveField(
            model_name='course',
            name='seat',
        ),
        migrations.RemoveField(
            model_name='course',
            name='semester',
        ),
        migrations.AddField(
            model_name='course',
            name='c_id',
            field=models.CharField(default='CN000', max_length=5, unique=True),
        ),
        migrations.AddField(
            model_name='course',
            name='max_seat',
            field=models.IntegerField(blank=True, default=5, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='seat_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='semmester',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='title',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='quota',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=64)),
                ('year', models.IntegerField()),
                ('courses', models.ManyToManyField(blank=True, related_name='attendances', to='courses.course')),
            ],
        ),
    ]
