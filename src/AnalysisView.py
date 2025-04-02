from dash import dcc, html
from .GraphingFunctions import create_tree_map
from dash import Input, Output

STAT_CSS = "card shadow-md rounded-2xl p-6 hover:scale-[1.01] transition duration-300 border border-gray-300"
STAT_LABEL = "text-sm font-medium text-gray-500"
STAT_VAL = "text-2xl font-bold text-gray-800 mt-1"
STAT_COUNT = "text-sm mt-2 text-success"


class GeneralAnalysis:
    def __init__(self, model, app):
        self.model = model
        self.app = app
        self.layout = self._create_layout()
        print(id(self.model))
        self._register_callbacks()

    def _create_layout(self):
        return html.Div(
            className="container mx-auto mb-10",
            children=[self._render_filter_section(), self._render_stats()],
        )

    def _render_filter_section(self):
        return html.Div(
            className="grid grid-cols-2 mx-auto card shadow-md rounded-2xl p-6 hover:scale-[1.01] transition duration-300 border border-gray-300 mb-4",
            children=[
                self._render_region_picker(),
                self._render_education_filter(),
            ],
        )

    def _render_stats(self):
        return html.Div(
            className="grid lg:grid-cols-4 gap-5",
            children=[
                self._render_total_emp_stat(),
                self._render_highest_emp_field(),
                self._render_field_highest_male(),
                self._render_field_highest_female(),
                self._render_field_employment(),
                self._render_field_highest_sex_ratio(),
                self._render_field_lowest_sex_ratio(),
            ],
        )

    def _render_total_emp_stat(self):
        return html.Div(
            className=STAT_CSS,
            children=[
                html.Label(
                    className=STAT_LABEL,
                    children="Total Employed Population",
                ),
                html.H3(
                    className=STAT_VAL,
                    id="total-emp-stat",
                    children="234,424",
                ),
            ],
        )

    def _render_highest_emp_field(self):
        return html.Div(
            className=STAT_CSS,
            children=[
                html.Label(
                    className=STAT_LABEL,
                    children="Field With Highest Employees",
                ),
                html.H3(
                    className=STAT_VAL,
                    id="highest-employe-field",
                    children="Legislative and senior management occupations",
                ),
                html.Label(
                    id="highest-employe-count",
                    className=STAT_COUNT,
                    children="43,1234",
                ),
            ],
        )

    def _render_field_highest_male(self):
        return html.Div(
            className=STAT_CSS,
            children=[
                html.Label(
                    className=STAT_LABEL,
                    children="Field With Highest Male Employees",
                ),
                html.H3(
                    className=STAT_VAL,
                    id="highest-male-field",
                    children="Legislative and se",
                ),
                html.Label(
                    id="highest-male-count",
                    className=STAT_COUNT,
                    children="43,1234",
                ),
            ],
        )

    def _render_field_highest_female(self):
        return html.Div(
            className=STAT_CSS,
            children=[
                html.Label(
                    className=STAT_LABEL,
                    children="Field With Highest Female Employees",
                ),
                html.H3(
                    className=STAT_VAL,
                    id="highest-female-field",
                    children="Legislative and se",
                ),
                html.Label(
                    id="highest-female-count",
                    className=STAT_COUNT,
                    children="43,1234",
                ),
            ],
        )

    def _render_field_highest_sex_ratio(self):
        return html.Div(
            className=STAT_CSS,
            children=[
                html.Label(
                    className=STAT_LABEL,
                    children="Field With Highest Sex Ratio",
                ),
                html.H3(
                    className=STAT_VAL,
                    id="highest-sex-ratio-field",
                    children="Legislative and se",
                ),
                html.Label(
                    id="highest-sex-ratio-count",
                    className=STAT_COUNT,
                    children="43,1234",
                ),
            ],
        )

    def _render_field_lowest_sex_ratio(self):
        return html.Div(
            className=STAT_CSS,
            children=[
                html.Label(
                    className=STAT_LABEL,
                    children="Field With Lowest Sex Ratio",
                ),
                html.H3(
                    className=STAT_VAL,
                    id="lowest-sex-ratio-field",
                    children="Legislative and se",
                ),
                html.Label(
                    id="lowest-sex-ratio-count",
                    className=STAT_COUNT,
                    children="43,1234",
                ),
            ],
        )

    def _render_field_employment(self):
        return html.Div(
            className=STAT_CSS + " col-span-3 row-span-2",
            children=[
                html.Label(
                    className=STAT_LABEL,
                    children="Regional Employment Trends",
                ),
                dcc.Graph(id="graph-employment-by-field"),
            ],
        )

    def _render_region_picker(self):
        province_list = self.model.get_province_list()
        return html.Div(
            className="z-[2] bg-white",
            children=[
                html.Label(
                    className="label-text font-medium text-gray-700 mb-2 font-bold",
                    children="Region",
                ),
                dcc.Dropdown(
                    id="province-selector-an1",
                    value=province_list[8],
                    options=province_list,
                    clearable=False,
                    className="w-96",
                ),
            ],
        )

    def _render_education_filter(self):
        return html.Div(
            className="",
            children=[
                html.Label(
                    className="label-text font-medium text-gray-700 mb-2 font-bold",
                    children="Education Level",
                ),
                dcc.RadioItems(
                    id="radio-education",
                    options={
                        "All": "All",
                        "Post secondary certificate, diploma or degree": "Post secondary certificate, diploma or degree",
                        "No Post secondary certificate, diploma or degree": "No Postsecondary certificate, diploma or degree",
                    },
                    value="All",
                ),
            ],
        )

    def _register_callbacks(self):

        @self.app.callback(
            [
                Output("total-emp-stat", "children"),
                Output("highest-employe-field", "children"),
                Output("highest-employe-count", "children"),
                Output("highest-male-field", "children"),
                Output("highest-male-count", "children"),
                Output("highest-female-field", "children"),
                Output("highest-female-count", "children"),
                Output("highest-sex-ratio-field", "children"),
                Output("highest-sex-ratio-count", "children"),
                Output("lowest-sex-ratio-field", "children"),
                Output("lowest-sex-ratio-count", "children"),
                Output("graph-employment-by-field", "figure"),
            ],
            [
                Input("province-selector-an1", "value"),
                Input("radio-education", "value"),
            ],
        )
        def handle_region_change(region, education):

            return (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, {})
