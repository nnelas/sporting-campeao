from dataclasses import dataclass, fields, astuple


@dataclass
class FootballTeam:
    position: int
    name: str
    logo_url_path: str
    played_games: int
    won: int
    draw: int
    lost: int
    points: int
    goals_for: int
    goals_against: int
    goal_difference: int
    form: str

    @staticmethod
    def get_headers() -> list:
        return [field.name for field in fields(FootballTeam)]

    def to_list(self) -> list:
        return list(astuple(self))
