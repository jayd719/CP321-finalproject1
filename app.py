import dash
from src.model import Model
from src.view import View
from src.controller import Controller
from src.setup import *
import os


app = dash.Dash(
    __name__,
    external_scripts=JS_SCRIPTS,
    external_stylesheets=SYTLE_SHEETS,
)
model = Model()
view = View()
Controller(app, model, view)
application = app.server

if __name__ == "__main__":
    app.run(debug=True)
