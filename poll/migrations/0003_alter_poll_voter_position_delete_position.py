# Generated by Django 4.1.3 on 2022-11-28 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_rename_prefect_name_poll_voter_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='voter_position',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Position',
        ),
    ]