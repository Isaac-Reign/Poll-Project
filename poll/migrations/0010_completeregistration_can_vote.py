# Generated by Django 4.1.3 on 2022-12-15 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0009_alter_poll_have_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='completeregistration',
            name='can_vote',
            field=models.BooleanField(default=True),
        ),
    ]