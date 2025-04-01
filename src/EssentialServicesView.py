from dash import dcc, html
from random import randint
from dash import Input, Output
from .GraphingFunctions import (
    create_gender_distribution_plot,
    create_gender_distribution_pie,
)


class EssentialSevericeDistribution:
    def __init__(self, model, app):
        self.model = model
        self.app = app
        self.layout = self._create_layout()
        self._register_callbacks()
        print(id(self.model))

    def _create_layout(self):
        return html.Div(
            className="bg-base-300 container mx-auto rounded-xl p-8 shadow-md hover-scale",
            children=[
                self._render_field_selector(),
                html.Div(
                    className="grid grid-cols-1 lg:grid-cols-4 gap-5",
                    children=[self._render_bar_chart(), self._render_pie_chart()],
                ),
            ],
        )

    def _render_bar_chart(self):
        return html.Div(
            className="grid gap-5 col-span-3 border p-4 border-gray-300 rounded-xl bg-base-100",
            children=[
                html.H2(
                    id="gender-bar-chart-header",
                    className="text-xl font-medium text-gray-700",
                    children="dddd",
                ),
                dcc.Graph(id="graph-gender-distribution", className=""),
                self._render_province_selector(),
            ],
        )

    def _render_pie_chart(self):
        return html.Div(
            className="pt-10 border p-4 border-gray-300 rounded-xl bg-base-100",
            children=[
                dcc.Graph(id="graph-gender-pie"),
                html.H3(
                    id="gender-pie-chart-header",
                    className="label-text font-medium text-gray-700 text-center",
                    children="dsf",
                ),
            ],
        )

    def _render_field_selector(self):
        feilds = self.model.get_field_list()
        return html.Div(
            className="flex justify-between items-center mb-10 z-[2]",
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
                    className="w-[500px]",
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
            [
                Output("graph-gender-distribution", "figure"),
                Output("graph-gender-pie", "figure"),
                Output("gender-bar-chart-header", "children"),
                Output("gender-pie-chart-header", "children"),
            ],
            [
                Input("field-selector", "value"),
                Input("province-selector", "value"),
            ],
        )
        def update_figure(field, province_list):
            df_by_province = self.model.get_gender_distribution_by_field(
                field, province_list
            )
            df_canada = self.model.get_gender_distribution_arsc(field)

            fig1 = create_gender_distribution_plot(df_by_province, field)
            fig2 = create_gender_distribution_pie(df_canada, field)

            title_bar = f"Gender Composition of  {field} Across Units"
            tiltle_pie = f"Gender Composition of  {field} Across Canada"
            return fig1, fig2, title_bar, tiltle_pie
