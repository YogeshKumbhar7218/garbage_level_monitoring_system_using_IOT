# Generated by Django 3.2.16 on 2023-02-23 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartbins', '0009_auto_20230223_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='smartbin',
            name='h_a_m_sent',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
