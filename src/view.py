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

from dash import dcc, html
import dash_mantine_components as dmc


class View:
    def __init__(
        self,
    ):
        # CONSTANTS
        self.title = "FIFA Soccer World Cup"
        self.subtitle = ""
        self.footerText = ""
        self.years = []

    def create_layout(self, years):
        self.years = years
        self.subtitle = f"Winners and Runner-ups from {min(years)} to {max(years)}"

        return html.Div(
            className="",
            children=[
                self._create_header(),
                self._create_controls(),
                dcc.Graph(id="output-map", figure={}),
                self._create_footer(),
            ],
        )

    def _create_header(self):
        return html.Div(
            children=[
                html.H1(
                    children=self.title,
                    className="text-4xl font-bold text-blue-800 mb-2",
                ),
                html.Span(
                    id="data-output",
                    className="text-lg text-gray-600",
                    children=self.subtitle,
                ),
                html.Hr(className="my-3"),
            ],
            className="my-10 container mx-auto",
        )

    def _create_footer(self):
        return html.Div(
            className="mt-16 mb-5 text-center text-gray-500",
            children=[html.Span(className="", children=self.footerText)],
        )

    def _create_controls(self):
        return html.Div(
            className="container mx-auto mb-5 grid grid-cols-3 gap-10",
            children=[
                self._create_dropdown_one(),
                self._create_count_control(),
                self._create_years_dropdown(),
            ],
        )

    def _create_dropdown_one(self):
        return dcc.Dropdown(
            id="controls-task-1",
            className="",
            options=["Winner", "Runner-ups", "Host"],
            value="Winner",
            clearable=False,
        )

    def _create_years_dropdown(self):
        return dcc.Dropdown(
            id="controls-year",
            className="",
            options=self.years,
            value="",
            placeholder="Select An Year",
        )

    def _create_count_control(self):
        return dcc.Checklist(
            id="single-checkbox",
            className="flex gap-2 border border-gray-300 p-1 rounded text-gray-500",
            options=[{"label": "Show Count", "value": "True"}],
            value=[],
        )
