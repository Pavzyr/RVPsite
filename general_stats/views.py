from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import GeneralStat


def index(request):
    template = 'general_stats/index.html'
    general_list = GeneralStat.objects.all()
    context = {'general_list': general_list}
    return render(request, template, context)
