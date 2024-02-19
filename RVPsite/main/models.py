from django.db import models


class GameId(models.Model):
    game_id = models.TextField(unique=True, blank=True, null=True)


class PashaPotnii(models.Model):
    key = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    game_id = models.ForeignKey(
        GameId,
        on_delete=models.CASCADE,
        related_name='pasha_potnii'
    )


class VladosKabardos(models.Model):
    key = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    game_id = models.ForeignKey(
        GameId,
        on_delete=models.CASCADE,
        related_name='vlados_cabardos'
    )


class EgorHardcore(models.Model):
    key = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    game_id = models.ForeignKey(
        GameId,
        on_delete=models.CASCADE,
        related_name='egor_hardcore'
    )


class MironPriton(models.Model):
    key = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    game_id = models.ForeignKey(
        GameId,
        on_delete=models.CASCADE,
        related_name='miron_priton'
    )


class VolodiaPodkidnoi(models.Model):
    key = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    game_id = models.ForeignKey(
        GameId,
        on_delete=models.CASCADE,
        related_name='volodia_podkidnoi'
    )

