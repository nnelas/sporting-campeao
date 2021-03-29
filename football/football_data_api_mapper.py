from http import HTTPStatus
from typing import List

import requests

from football.football_data_api_response import FootballDataApiResponse
from football.football_team import FootballTeam


class FootballDataApiMapper:
    def __init__(self):
        pass

    def map(self, response: requests.Response) -> FootballDataApiResponse:
        if response.status_code == HTTPStatus.OK:
            standings = self.__to_dataclass(response.json()["standings"][0])
            return FootballDataApiResponse(HTTPStatus.OK, standings)
        return FootballDataApiResponse(HTTPStatus.BAD_REQUEST)

    def __to_dataclass(self, standings: dict) -> List[FootballTeam]:
        standings_dataclass = []
        for team in standings["table"]:
            standings_dataclass.append(
                FootballTeam(
                    position=int(team["position"]),
                    name=team["team"]["name"],
                    logo_url_path=team["team"]["crestUrl"],
                    played_games=int(team["playedGames"]),
                    won=int(team["won"]),
                    draw=int(team["draw"]),
                    lost=int(team["lost"]),
                    points=int(team["points"]),
                    goals_for=int(team["goalsFor"]),
                    goals_against=int(team["goalsAgainst"]),
                    goal_difference=int(team["position"]),
                    form=team["form"],
                )
            )

        return standings_dataclass
