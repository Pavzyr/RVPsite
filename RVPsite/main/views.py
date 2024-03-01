from django.shortcuts import render
from django.db.models import Sum, IntegerField, Subquery, OuterRef
from django.db.models.expressions import RawSQL
from django.db.models.functions import Cast

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
    player_nicks = ['ВЛАДОС КАБАРДОС', 'ПАША ПОТНЫЙ', 'ЕГОР ХАРДКОР', 'МИРОН ПРИТОН', 'ВОЛОДЯ ПОДКИДНОЙ']
    general_stat_vova = get_general_stat(player_nicks[4])
    general_stat_pasha = get_general_stat(player_nicks[1])
    context = {
        'view_name': request.resolver_match.view_name,
        'general_stat_pasha': general_stat_pasha,
        'general_stat_vova': general_stat_vova,
        }
    return render(request, template, context)


def game_detail(request, game_id):
    template = 'pages/game_page.html'
    game_list = GameStat.objects.filter(game_id=game_id).values('player_nick').distinct()

    # Подзапрос для получения значений value в одном ряду со значением championName
    subquery = GameStat.objects.filter(
        game_id=game_id,
        player_nick=OuterRef('player_nick'),
        key='championName'
        ).values('value')[:1]

    # Запрос для получения уникальных ников и значений value
    player_stats = GameStat.objects.filter(game_id=game_id).values('player_nick').distinct().annotate(
        champion_value=Subquery(RawSQL(subquery.query, subquery.params))
    )
    print(player_stats)
    context = {
        'game_list': game_list,
        } 
    return render(request, template, context)


def refresh_game_id(request):
    RiotAPI().get_game_ids()
    return index(request)


def get_general_stat(nick: str):
    general_stat = GameStat.objects.filter(player_nick=nick).values('key').annotate(total_value=Sum(Cast('value', output_field=IntegerField()))).distinct()
    return general_stat
