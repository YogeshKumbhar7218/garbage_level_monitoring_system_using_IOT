# Generated by Django 3.2.16 on 2022-11-13 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bin_number', models.SmallIntegerField(unique=True)),
                ('filled', models.SmallIntegerField()),
                ('location', models.TextField()),
                ('depth', models.SmallIntegerField()),
                ('under_employee', models.SmallIntegerField()),
            ],
        ),
    ]
