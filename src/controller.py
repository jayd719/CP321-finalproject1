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

        self.app.layout = self.view.create_layout(self.model.years())
        # self._register_callbacks()

    def _register_callbacks(self):
        """Register all Dash callbacks"""

        @self.app.callback(
            Output("choropleth-map", "figure"),
            [
                Input("color-scale", "value"),
                Input("scope", "value"),
                Input("pop-slider", "value"),
            ],
        )
        def update_map(color_scale, scope, min_pop):
            filtered_df = self.model.get_filtered_data(min_pop)

            fig = px.choropleth(
                filtered_df,
                locations="Code",
                locationmode="USA-states",
                color="Population",
                scope=scope,
                color_continuous_scale=color_scale,
                title=f"US States with Population ≥ {min_pop} Million",
                hover_name="State",
                hover_data={"Code": False, "Population": ":,f"},
                range_color=[
                    filtered_df["Population"].min(),
                    filtered_df["Population"].max(),
                ],
            )

            fig.update_layout(
                margin={"r": 0, "t": 40, "l": 0, "b": 0},
                geo=dict(bgcolor="rgba(0,0,0,0)"),
                plot_bgcolor="rgba(0,0,0,0)",
            )

            return fig

        @self.app.callback(
            Output("state-info", "children"), [Input("choropleth-map", "clickData")]
        )
        def display_click_data(click_data):
            return self.view.create_state_info(click_data)
