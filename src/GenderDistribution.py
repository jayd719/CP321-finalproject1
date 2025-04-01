from dash import dcc, html

state_list = [1, 3, 4, 5, 6, 7, 8, 9]


class GenderDistribution:
    def __init__(self, model):
        self.model = model
        self.layout = self._create_layout()

    def _create_layout(self):
        return html.Div(
            className="card bg-white container mx-auto rounded-xl p-6 shadow-soft hover-scale",
            children=[
                self._render_field_selector(),
                self._render_province_selector(),
            ],
        )

    def _render_field_selector(self):
        return html.Div(
            className="flex justify-between items-center mb-6",
            children=[
                html.H2(
                    className="text-xl font-semibold text-gray-800",
                    children="Gender Distribution by Field",
                ),
                dcc.Dropdown(
                    id="field-selector",
                    options=["Gold", "MediumTurquoise", "LightGreen"],
                    value="Gold",
                    clearable=False,
                    className="w-96 opacity-75",
                ),
            ],
        )

    def _render_province_selector(self):
        return html.Div(
            children=[
                dcc.Dropdown(
                    id="bar-polar-app-x-dropdown",
                    value=state_list[:6],
                    options=state_list,
                    multi=True,
                ),
            ],
        )
