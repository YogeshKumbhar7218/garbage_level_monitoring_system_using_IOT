# Generated by Django 3.2.16 on 2022-11-14 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartbins', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='filled',
        ),
        migrations.AddField(
            model_name='user',
            name='dry_filled',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='wet_filled',
            field=models.SmallIntegerField(null=True),
        ),
    ]
