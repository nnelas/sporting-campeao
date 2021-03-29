import os
from typing import Optional

from football.football_data_api import FootballDataApi
from football.football_data_api_mapper import FootballDataApiMapper
from football.football_data_repository import FootballDataRepository


class FootballProvider:
    def __init__(self):
        self.__football_data_api = FootballDataApi(
            "http://api.football-data.org",
            self.__get_football_data_api_key,
            FootballDataApiMapper(),
        )

    def provide_football_data_repository(self) -> FootballDataRepository:
        return FootballDataRepository(self.__football_data_api)

    @property
    def __get_football_data_api_key(self) -> Optional[str]:
        if os.getenv("FOOTBALL_DATA_API_KEY") is None:
            raise Exception(
                "Unable to get FOOTBALL_DATA_API_KEY. Please make sure that "
                "you have added it into your environment variables."
            )
        return os.getenv("FOOTBALL_DATA_API_KEY")


football_provider = FootballProvider()
