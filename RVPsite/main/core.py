from riotwatcher import LolWatcher
from .models import GameId, GameStat


class RiotAPI():
    def __init__(self):
        self.riot_api_key = 'RGAPI-6f36ce44-b388-4837-b34e-667038f017ef'
        self.eur_API = 'europe.api.riotgames.com'
        self.ru_API = 'ru.api.riotgames.com'
        self.puuids = {
            'vova': 'IRJUVG25-WHbhOZt2zQe8KycTrThPhuawR2Wm2DXxUHruxYni_S3VYcjZvTGNPtkZX4gMFa2pCSUgA',
            'pasha': '5FvlCp0NC_pITDbzYri0SpjqB-mshAKeM9A7UDGubLQ36wb9QMfbfKy4hLlB6lJn3SjINmWX4wJz-g',
            'vlad': 'hb7xNtaOslUs7R6hSJVvZuTbM8bmJqBsCUv_L1lC17WANMbt1Xtbd_UpZZhWrh4iztqb995Q8hbBYw',
            'egor': 'vMAbdWcWOqMmYDI0vS1POPdC_rgHMjxmd_rafripnZlOQriRrK11KxJuVcAnrsE5udMu82hQJPD84Q',
            'serg': 'k92rFMH-JFo6511okkCWKoVJaFBShROuscFJNfD7uw0LQtUTjFhVuaSoZ-YEYqYx6MA2XV-zU2c-Vw',
        }

    def get_game_ids(self):
        # Работа с АПИ
        watcher = LolWatcher(self.riot_api_key)
        my_matches = watcher.match.matchlist_by_puuid(
            'ru',
            self.puuids['serg']
            )
        my_matches += [
            'RU_477379073',
            'RU_477367687',
            'RU_477359894',
            'RU_477160378',
            'RU_477157257',
            'RU_477148928',
            'RU_476839568',
            'RU_476832638',
            'RU_476829242',
            'RU_476757259',
            'RU_476748918',
            'RU_476619479',
            'RU_476610916',
            'RU_475709685',
            'RU_474404901',
            'RU_474399846',
            'RU_474397641',
            'RU_477747599',
            'RU_477736859',
            'RU_477730386',
        ]
        for match in my_matches:
            if GameId.objects.filter(game_id=match).exists():
                print(f'Match "{match}" already exist')
            else:
                match_detail = watcher.match.by_id('ru', match)
                participants = match_detail['metadata']['participants']
                self_stat = match_detail['info']['participants']
                if all(puuid in participants for puuid in self.puuids.values()):
                    GameId.objects.update_or_create(game_id=match)
                    stat_list = []
                    for player in self_stat:
                        for player_stat in player:
                            if isinstance(player[player_stat], dict):
                                for key in player[player_stat]:
                                    stat_list.append(GameStat(player_nick=player['summonerName'], key=key, value=player[player_stat][key], game_id=match))
                            else:
                                stat_list.append(GameStat(player_nick=player['summonerName'], key=player_stat, value=player[player_stat], game_id=match))
                    GameStat.objects.bulk_create(stat_list)
                    print(f'Match "{match}" has been added')
        print('All DATA has been added')