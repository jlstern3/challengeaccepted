# Generated by Django 2.2 on 2021-04-14 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges_app', '0002_user_goals'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='unit_measure',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='starting_at',
            field=models.IntegerField(),
        ),
    ]
