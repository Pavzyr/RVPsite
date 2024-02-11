import django_tables2 as tables
from .models import GeneralStat

class PersonTable(tables.Table):
    class Meta:
        model = GeneralStat
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", )