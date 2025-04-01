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
DATASOURCE_URL = "/Users/jashan/Desktop/CP321-FinalProject/data/finalData.csv"


app = dash.Dash(
    __name__,
    external_scripts=JS_SCRIPTS,
    external_stylesheets=SYTLE_SHEETS,
)


model = Model(DATASOURCE_URL)
view = View()

app.title = "CP321 Final Project"

Controller(app, model, view)


application = app.server

if __name__ == "__main__":
    app.run(debug=True)
