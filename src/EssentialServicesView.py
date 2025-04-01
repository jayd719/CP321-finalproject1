from dash import dcc, html
from random import randint
from dash import Input, Output, ctx
from .GraphingFunctions import create_polar_essentails


class EssentialSevericeDistribution:
    def __init__(self, model, app):
        self.model = model
        self.app = app
        self.layout = self._create_layout()
        self._register_callbacks()
        print(id(self.model))

    def _create_layout(self):
        return html.Div(
            className="bg-base-200 container mx-auto rounded-xl p-8 shadow-xl hover-scale mb-10",
            children=[
                html.Div(
                    className="grid grid-cols-1 lg:grid-cols-4 gap-5",
                    children=[
                        self._render_buttons(),
                        self._render_distribution_chart(),
                    ],
                ),
            ],
        )

    def _render_buttons(self):
        children = []
        for button in self.model.get_list_of_essential_occ():
            button_id = button
            children.append(
                html.Button(
                    id=button_id, className="btn btn-soft btn-primary", children=button
                )
            )
        return html.Div(className="grid grid-cols-1", children=children)

    def _render_distribution_chart(self):
        df = self.model.get_essentails_df_whole()
        fig = create_polar_essentails(df)

        return html.Div(
            className="pt-10 border p-4 border-gray-300 rounded-xl bg-base-100 col-span-3",
            children=[
                dcc.Graph(id="essentials-chart", figure=fig),
            ],
        )

    def _register_callbacks(self):

        @self.app.callback(
            Output("essentials-chart", "figure"),
            [Input(f"{i}", "n_clicks") for i in self.model.get_list_of_essential_occ()],
        )
        def hangle_click(*args):
            if ctx.triggered_id:
                print(ctx.triggered_id)
            return None
