from dash import dcc, html
from .GraphingFunctions import create_tree_map


class ManpowerDistribution:
    def __init__(self, model, app):
        self.model = model
        self.app = app
        self.layout = self._create_layout()
        print(id(self.model))

    def _create_layout(self):
        df = self.model.get_engineering_df()
        fig = create_tree_map(df)
        return html.Div(
            className="bg-base-300 container mx-auto rounded-xl p-10 shadow-md hover-scale mt-10",
            children=[
                html.H2(
                    className="text-xl font-semibold text-gray-800",
                    children="Manpower Analysis for EV Factory Location: Comparing Administrative Units",
                ),
                html.Div(
                    className="grid p-10 rounded-xl",
                    children=[
                        dcc.Graph(id="manpower-chart", figure=fig),
                    ],
                ),
            ],
        )
