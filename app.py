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
from dash import html
from src.model import Model
from src.GenderDistributionView import GenderDistribution
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
task02 = GenderDistribution(model, app)

app.title = "CP321 Final Project"
app.layout = [
    html.Div(
        children=[
            html.Div(id="header"),
            html.Div(
                className="pt-20",
                children=[task02.layout],
            ),
            html.Div(id="footer"),
        ]
    )
]

application = app.server
if __name__ == "__main__":
    app.run(debug=True)
