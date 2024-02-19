from django.shortcuts import render

from .models import GameId
from .forms import GameIdInput
from django.http import HttpResponse


def index(request):
    template = 'pages/index.html'
    game_id_form = GameIdInput(request.POST or None)
    post_list = GameId.objects.all()
    context = {
        'post_list': post_list,
        'view_name': request.resolver_match.view_name,
        'game_id_form': game_id_form,
        'game_id_form': game_id_form,

        }
    if game_id_form.is_valid():
        game_id_form.save() 
    return render(request, template, context)


def general_stats(request):
    template = 'pages/general_stats.html'
    context = {
        'view_name': request.resolver_match.view_name
        }
    return render(request, template, context)


def game_detail(request, game_id):
    return HttpResponse(f'Категория {game_id}') 
