import datetime
import locale

from flask import Flask, render_template
from flask_talisman import Talisman

from football.football_provider import football_provider
from football.supported_leagues import SupportedLeagues

csp = {"default-src": ["'self'", "cdn.jsdelivr.net", "cdnjs.cloudflare.com"]}

app = Flask(__name__)
Talisman(app, content_security_policy=csp)
football_data_repository = football_provider.provide_football_data_repository()


@app.route("/")
def index():
    locale.setlocale(locale.LC_TIME, "pt_PT.UTF-8")
    date = datetime.date.today().strftime("%d de %B de %Y")
    message = "ainda não"
    response = football_data_repository.get_league_standings(
        SupportedLeagues.PT_PRIMEIRA_LIGA
    )
    return render_template(
        "index.html",
        date_string=date,
        is_champ_string=message,
        headers=response[0].get_headers(),
        objects=response,
    )
