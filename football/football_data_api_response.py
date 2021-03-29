from dataclasses import dataclass
from http import HTTPStatus
from typing import List

from football.football_team import FootballTeam


@dataclass
class FootballDataApiResponse:
    status: HTTPStatus
    football_team: List[FootballTeam] = None
