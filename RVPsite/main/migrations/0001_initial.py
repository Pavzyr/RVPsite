# Generated by Django 3.2 on 2024-02-19 08:01

from django.db import migrations, models
import django.db.models.deletion


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
            name='VolodiaPodkidnoi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.TextField(blank=True, null=True)),
                ('value', models.TextField(blank=True, null=True)),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='volodia_podkidnoi', to='main.gameid')),
            ],
        ),
        migrations.CreateModel(
            name='VladosKabardos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.TextField(blank=True, null=True)),
                ('value', models.TextField(blank=True, null=True)),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vlados_cabardos', to='main.gameid')),
            ],
        ),
        migrations.CreateModel(
            name='PashaPotnii',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.TextField(blank=True, null=True)),
                ('value', models.TextField(blank=True, null=True)),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pasha_potnii', to='main.gameid')),
            ],
        ),
        migrations.CreateModel(
            name='MironPriton',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.TextField(blank=True, null=True)),
                ('value', models.TextField(blank=True, null=True)),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='miron_priton', to='main.gameid')),
            ],
        ),
        migrations.CreateModel(
            name='EgorHardcore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.TextField(blank=True, null=True)),
                ('value', models.TextField(blank=True, null=True)),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='egor_hardcore', to='main.gameid')),
            ],
        ),
    ]
