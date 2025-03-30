"""-------------------------------------------------------
CP321: Assignment 7- App.py
-------------------------------------------------------
Author:  JD
ID:      169018282
Uses:    pandas,numpy,plotly,dash
Version:  1.0.8
__updated__ = Sun Mar 30 2025
-------------------------------------------------------
"""

# Imports

import dash
from src.model import Model
from src.view import View
from src.controller import Controller
from src.setup import *
import os


# CONTANTS
DATASOURCE_URL = "https://en.wikipedia.org/wiki/List_of_FIFA_World_Cup_finals"
TABLE_ID = "plainrowheaders"


app = dash.Dash(
    __name__,
    external_scripts=JS_SCRIPTS,
    external_stylesheets=SYTLE_SHEETS,
)


model = Model(DATASOURCE_URL, TABLE_ID)
view = View()
Controller(app, model, view)


application = app.server

if __name__ == "__main__":
    app.run(debug=True)
