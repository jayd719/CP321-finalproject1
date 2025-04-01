from dash import dcc, html
from random import randint
from dash import Input, Output
from .GraphingFunctions import create_gender_distribution_plot


class GenderDistribution:
    def __init__(self, model, app):
        self.model = model
        self.app = app
        self.layout = self._create_layout()
        self._register_callbacks()
        print(id(self.model))

    def _create_layout(self):
        return html.Div(
            className="card bg-white container mx-auto rounded-xl p-6 shadow-soft hover-scale",
            children=[
                self._render_field_selector(),
                self._renden_figure(),
                self._render_province_selector(),
            ],
        )

    def _renden_figure(self):
        return html.Div(
            className="",
            children=[
                dcc.Graph(id="graph-gender-distribution"),
            ],
        )

    def _render_field_selector(self):
        feilds = self.model.get_field_list()
        return html.Div(
            className="flex justify-between items-center mb-6 z-[2]",
            children=[
                html.H2(
                    className="text-xl font-semibold text-gray-800",
                    children="Gender Distribution by Field",
                ),
                dcc.Dropdown(
                    id="field-selector",
                    options=feilds,
                    value=feilds[randint(0, len(feilds) - 1)],
                    clearable=False,
                    className="w-[500px] brightness-90",
                ),
            ],
        )

    def _render_province_selector(self):
        province_list = self.model.get_province_list()
        return html.Div(
            children=[
                dcc.Dropdown(
                    id="province-selector",
                    value=province_list[:10],
                    options=province_list,
                    multi=True,
                    clearable=False,
                ),
            ],
        )

    def _register_callbacks(self):

        @self.app.callback(
            Output("graph-gender-distribution", "figure"),
            [
                Input("field-selector", "value"),
                Input("province-selector", "value"),
            ],
        )
        def update_figure(field, province_list):
            df = self.model.get_gender_distribution_by_field(field, province_list)
            return create_gender_distribution_plot(df, field)
