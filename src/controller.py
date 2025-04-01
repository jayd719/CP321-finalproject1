"""-------------------------------------------------------
CP321: Assignment 7 - Controller.py
-------------------------------------------------------
Author:  JD
ID:      169018282
Uses:    pandas,numpy,plotly,dash
Version:  1.0.8
__updated__ = Sun Mar 30 2025
-------------------------------------------------------
"""

from dash import Input, Output
from .GenderDistribution import GenderDistribution
from dash import dcc, html, dash_table


class Controller:
    def __init__(self, app, model, view):
        self.app = app
        self.model = model
        self.app01 = GenderDistribution(self.model)

        self.app.layout = self._create_layout()
        # self._register_callbacks()

    def _create_layout(self):
        return html.Div(
            children=[
                html.Div(id="header"),
                self._render_app(),
                html.Div(id="footer"),
            ]
        )

    def _render_app(self):
        return html.Div(
            className="pt-20",
            children=[self.app01.layout],
        )
