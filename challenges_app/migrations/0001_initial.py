# Generated by Django 2.2 on 2021-04-18 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('age', models.IntegerField(null=True)),
                ('location', models.TextField(null=True)),
                ('quote', models.TextField(null=True)),
                ('goals', models.TextField(null=True)),
                ('email', models.TextField()),
                ('password', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('description', models.TextField()),
                ('target_area', models.CharField(max_length=45)),
                ('starting_at', models.IntegerField()),
                ('daily_increase', models.IntegerField()),
                ('unit_measure', models.TextField(null=True)),
                ('max_reps', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('users_accepted', models.ManyToManyField(related_name='challenges_accepted', to='challenges_app.User')),
                ('users_completed', models.ManyToManyField(related_name='challenges_completed', to='challenges_app.User')),
            ],
        ),
    ]
