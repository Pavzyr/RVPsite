from django.shortcuts import render

from .models import GameId, GameStat
from .core import RiotAPI


def index(request):
    template = 'pages/index.html'
    post_list = GameId.objects.all()
    context = {
        'post_list': post_list,
        'view_name': request.resolver_match.view_name,
        } 
    return render(request, template, context)


def general_stats(request):
    template = 'pages/general_stats.html'
    context = {
        'view_name': request.resolver_match.view_name
        }
    return render(request, template, context)


def game_detail(request, game_id):
    template = 'pages/game_page.html'
    game_list = GameStat.objects.filter(game_id=game_id).values('player_nick').distinct()
    context = {
        'game_list': game_list,
        } 
    return render(request, template, context)


def refresh_game_id(request):
    RiotAPI().get_game_ids()
    return index(request)
