# Generated by Django 3.0.5 on 2020-05-19 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eye_aspect_ratio', models.CharField(max_length=20)),
                ('time_alarm_raised', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
