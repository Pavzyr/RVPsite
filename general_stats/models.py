from django.db import models


class GeneralStat(models.Model):
    key = models.TextField(blank=True, null=True)
    volod9_podkidnoi = models.TextField(db_column='VOLOD9_PODKIDNOI', blank=True, null=True)  # Field name made lowercase.
    pasha_potnii = models.TextField(db_column='PASHA_POTNII', blank=True, null=True)  # Field name made lowercase.
    vlados_cabardos = models.TextField(db_column='VLADOS_CABARDOS', blank=True, null=True)  # Field name made lowercase.
    egor_hardcore = models.TextField(db_column='EGOR_HARDCORE', blank=True, null=True)  # Field name made lowercase.
    miron_priton = models.TextField(db_column='MIRON_PRITON', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GENERAL_STAT'
