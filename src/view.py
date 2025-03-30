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
import plotly.express as px


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
                dcc.Graph(id="output-map", figure={}, className=""),
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
            options=["Winners", "Runners-up", "Host"],
            value="Winners",
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
            id="count-checkbox",
            className="flex gap-2 border border-gray-300 p-1 rounded text-gray-500",
            options=[{"label": "Show Count", "value": "True"}],
            value=[],
        )

    def _update_common(self, fig, filter):
        title = f"FIFA World Cup {filter}"
        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(family="Arial", size=15, color="#333333"),
            title={
                "text": title,
                "y": 0.95,
                "x": 0.5,
                "font": dict(size=20, color="#333333"),
            },
            margin=dict(l=2, r=2, t=50, b=2),
            hoverlabel=dict(bgcolor="white", font_size=14, font_family="Arial"),
        )
        return fig

    def create_map(self, df, filter):
        fig = px.choropleth(
            df,
            locations="Country",
            locationmode="country names",
            hover_name="Country",
            hover_data={f"{filter}": True, "Country": True},
            projection="natural earth",
            labels={f"{filter}": f"Number of Times {filter} "},
            height=600,
        )
        fig = self._update_common(fig, filter)
        return fig

    def create_map_with_counts(self, df, filter):
        df[filter] = df[filter].astype(str)
        fig = px.choropleth(
            df,
            locations="Country",
            locationmode="country names",
            color=f"{filter}",
            hover_name="Country",
            hover_data={f"{filter}": True, "Country": True},
            projection="natural earth",
            labels={f"{filter}": f"Number of Times {filter} "},
            height=600,
        )

        fig = self._update_common(fig, filter)
        fig.update_layout(
            coloraxis_colorbar={
                "title": f"{filter} Count",
                "thickness": 15,
                "len": 0.75,
                "x": 0.9,
                "y": 0.5,
                "yanchor": "middle",
                "tickfont": dict(size=13),
                "title_font": dict(size=16),
            },
        )

        return fig

    def create_map_by_year(self, df, year):
        title = f"Winners, Runner-Up and Host For Year {year}"
        fig = px.choropleth(
            df,
            locations="Country",
            locationmode="country names",
            color="Category",
            hover_name="Country",
            projection="natural earth",
            height=600,
        )

        fig = self._update_common(fig, title)
        return fig
