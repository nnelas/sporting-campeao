import logging
from http import HTTPStatus

import requests

from football.football_data_api_mapper import FootballDataApiMapper
from football.football_data_api_response import FootballDataApiResponse
from football.supported_leagues import SupportedLeagues


class FootballDataApi:
    def __init__(
        self,
        base_host: str,
        api_token: str,
        football_data_api_mapper: FootballDataApiMapper,
        timeout: int = 5,
        logger: logging.Logger = logging.getLogger("FootballDataApi"),
    ):
        self.__base_host = base_host
        self.__football_data_api_mapper = football_data_api_mapper
        self.__auth_headers = {"X-Auth-Token": api_token}
        self.__timeout = timeout
        self.__logger = logger

    def get_league_standings(self, league: SupportedLeagues) -> FootballDataApiResponse:
        try:
            url = self.__base_host + f"/v2/competitions/{league.value}/standings"
            response = requests.get(
                url, headers=self.__auth_headers, timeout=self.__timeout
            )
            return self.__football_data_api_mapper.map(response)
        except (
            requests.exceptions.ConnectionError,
            requests.exceptions.ReadTimeout,
        ) as e:
            self.__logger.warning(f"Couldn't connect to FootballDataApi: '{str(e)}'")
            return FootballDataApiResponse(HTTPStatus.INTERNAL_SERVER_ERROR)
