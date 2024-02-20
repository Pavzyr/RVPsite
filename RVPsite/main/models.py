from django.db import models


class GameId(models.Model):
    game_id = models.TextField(unique=True, blank=True, null=True)


class GameStat(models.Model):
    player_nick = models.TextField(blank=True, null=True)
    key = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    game_id = models.TextField(blank=True, null=True)
