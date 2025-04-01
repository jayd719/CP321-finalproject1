"""-------------------------------------------------------
CP321: Assignment 7- View.py
-------------------------------------------------------
Author:  JD
ID:      169018282
Uses:    pandas,numpy,plotly,dash
Version:  1.0.8
__updated__ = Sun Mar 30 2025
-------------------------------------------------------
"""

from dash import dcc, html, dash_table
import plotly.express as px


class View:
    def __init__(self):
        self.years = []

    def create_layout(self):
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
            children=[],
        )
