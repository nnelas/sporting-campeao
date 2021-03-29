from http import HTTPStatus
from typing import List

from football.football_data_api import FootballDataApi
from football.football_team import FootballTeam
from football.supported_leagues import SupportedLeagues


class FootballDataRepository:
    def __init__(self, football_data_api: FootballDataApi):
        self.__football_data_api = football_data_api

    def get_league_standings(self, league: SupportedLeagues) -> List[FootballTeam]:
        response = self.__football_data_api.get_league_standings(league)
        if response.status == HTTPStatus.OK:
            return response.football_team
        return []
