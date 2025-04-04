"""-------------------------------------------------------
CP321: Final Project components.py
-------------------------------------------------------
Author:  JD
ID:      169018282
Uses:    pandas,numpy,plotly,dash
Version:  1.0.8
__updated__ = Sun Mar 30 2025
-------------------------------------------------------
"""

from dash import html


def render_dashboard_header():
    return html.Div(
        className="container mx-auto mb-10 mt-5",
        children=[
            html.H1(
                className="text-2xl font-bold text-gray-800",
                children="Workforce Distribution and Occupational Trends Across Canadian Provinces and Territories",
            ),
            html.Span(
                className="text-gray-600",
                children=[
                    "Data Source: Statistics Canada, 2021 Census (Table: 98-10-0404-01)",
                ],
            ),
        ],
    )
