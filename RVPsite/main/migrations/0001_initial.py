# Generated by Django 4.2.10 on 2024-02-20 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_id', models.TextField(blank=True, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='GameStat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_nick', models.TextField(blank=True, null=True)),
                ('key', models.TextField(blank=True, null=True)),
                ('value', models.TextField(blank=True, null=True)),
                ('game_id', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
