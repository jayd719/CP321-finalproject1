from dash import dcc, html


class View:

    def __init__(self):
        self.title = "FIFA Soccer World Cup"
        self.subtitle = "Winners and Runner-ups from 1930 to 2022"
        self.footerText = "Data sourced from Wikipedia. Last updated: 2023"

        self.layout = self._create_layout()

    def _create_layout(self):
        """Create and return the app layout"""
        return html.Div(
            className="",
            children=[
                self._create_header(),
                html.Div(
                    className="container mx-auto",
                    children=[
                        self._create_controls_column1(),
                        self._create_controls_column2(),
                        self._create_controls_column3(),
                    ],
                    style={"borderBottom": "thin lightgrey solid", "padding": "10px"},
                ),
                dcc.Graph(id="choropleth-map"),
                html.Div(id="state-info", style={"marginTop": 20, "padding": "10px"}),
                self._create_footer(),
            ],
        )

    def _create_header(self):
        return html.Div(
            children=[
                html.H1(
                    children=self.title,
                    className="font-title relative z-2 text-3xl leading-none font-black text-primary",
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

    def _create_controls_column1(self):
        """Create color scale dropdown"""
        return html.Div(
            [
                html.Label("Select Color Scale:"),
                dcc.Dropdown(
                    id="color-scale",
                    options=[
                        {"label": "Viridis", "value": "Viridis"},
                        {"label": "Plasma", "value": "Plasma"},
                        {"label": "Rainbow", "value": "Rainbow"},
                        {"label": "Electric", "value": "Electric"},
                        {"label": "Hot", "value": "Hot"},
                    ],
                    value="Viridis",
                    clearable=False,
                ),
            ],
            style={"width": "30%", "display": "inline-block", "padding": "10px"},
        )

    def _create_controls_column2(self):
        """Create scope radio buttons"""
        return html.Div(
            [
                html.Label("Map Scope:"),
                dcc.RadioItems(
                    id="scope",
                    options=[
                        {"label": "USA", "value": "usa"},
                        {"label": "North America", "value": "north america"},
                    ],
                    value="usa",
                    inline=True,
                ),
            ],
            style={"width": "30%", "display": "inline-block", "padding": "10px"},
        )

    def _create_controls_column3(self):
        """Create population slider"""
        return html.Div(
            [
                html.Label("Minimum Population (millions):"),
                dcc.Slider(
                    id="pop-slider",
                    min=5,
                    max=40,
                    step=1,
                    value=5,
                    marks={i: str(i) for i in range(5, 41, 5)},
                ),
            ],
            style={"width": "35%", "display": "inline-block", "padding": "10px"},
        )

    def create_state_info(self, click_data):
        """Create state information display"""
        if click_data is None:
            return "Click on a state to see more details"

        state = click_data["points"][0]["hovertext"]
        population = click_data["points"][0]["customdata"][0]

        return html.Div(
            [
                html.H3(f"{state}"),
                html.P(f"Population: {population:,}"),
                html.P(f"State Code: {click_data['points'][0]['location']}"),
            ]
        )
