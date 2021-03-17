import datetime
import locale

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    locale.setlocale(locale.LC_TIME, "pt_PT.UTF-8")
    date = datetime.date.today().strftime("%d de %B de %Y")
    message = "ainda não"
    return render_template("index.html", date_string=date, is_champ_string=message)
