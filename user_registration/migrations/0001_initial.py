# Generated by Django 3.0.5 on 2020-04-21 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_registration_number', models.CharField(max_length=10)),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
    ]
