# Generated by Django 3.2.16 on 2022-11-18 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartbins', '0004_rename_depth_smartbin_height'),
    ]

    operations = [
        migrations.AddField(
            model_name='smartbin',
            name='map_location',
            field=models.TextField(null=True),
        ),
    ]
