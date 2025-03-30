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

import plotly.express as px
from dash import Input, Output


class Controller:
    def __init__(self, app, model, view):
        self.app = app
        self.model = model
        self.view = view

        self.view.footerText = "Data sourced from Wikipedia. Last updated: 2025"

        self.app.layout = self.view.create_layout(self.model.get_years())
        self._register_callbacks()

    def _register_callbacks(self):
        """Register all Dash callbacks"""

        @self.app.callback(
            Output("output-map", "figure"),
            Input("controls-task-1", "value"),
            Input("count-checkbox", "value"),
        )
        def update_map(filter_col, checkbox):
            df = self.model.get_counts(filter_col)

            if len(checkbox):
                fig = self.view.create_map_with_counts(df, filter_col)
            else:
                fig = self.view.create_map(df, filter_col)
            return fig

        @self.app.callback(
            Output("output-map", "figure", allow_duplicate=True),
            Input("controls-year", "value"),
            prevent_initial_call=True,
        )
        def update_map_year(year):
            df = self.model.get_by_year(str(year))
            return self.view.create_map_by_year(df, year)
