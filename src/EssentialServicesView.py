from dash import dcc, html
from random import randint
from dash import Input, Output, ctx
from .GraphingFunctions import create_polar_essentails, create_essentials_pie


class EssentialSevericeDistribution:
    def __init__(self, model, app):
        self.model = model
        self.app = app
        self.layout = self._create_layout()
        self._register_callbacks()
        print(id(self.model))

    def _create_layout(self):
        return html.Div(
            className="container mx-auto card shadow-md hover:shadow-xl rounded-2xl p-6  transition duration-300 border border-gray-100 my-20",
            children=[
                html.Div(
                    children=[
                        html.H2(
                            className="text-xl font-bold mb-5 text-primary",
                            children="Distribution of Essential Service Human Resources Across Administrative Units",
                        ),
                        html.Div(
                            className="grid grid-cols-1 lg:grid-cols-3 gap-5",
                            children=[
                                self._render_buttons(),
                                self._render_distribution_chart(),
                            ],
                        ),
                        self._render_reset_button(),
                    ]
                )
            ],
        )

    def _render_reset_button(self):
        return html.Div(
            id="",
            className="flex justify-between items-center my-2 z-[2]",
            children=[
                html.H2(
                    className="",
                    children=" ",
                ),
                html.Button(
                    id="reset-essential-dis",
                    className="btn btn-sm btn-error",
                    children="Reset",
                ),
            ],
        )

    def _render_buttons(self):
        children = []
        for button in self.model.get_list_of_essential_occ():
            button_id = button
            children.append(
                html.Button(
                    id=button_id,
                    className="btn btn btn-outline btn-sm text-xs",
                    children=button,
                )
            )

        return html.Div(
            className="grid grid-cols-1 p-3 border p-4 border-gray-100 rounded-xl",
            children=children,
        )

    def _render_distribution_chart(self):
        return html.Div(
            className="border p-4 border-gray-100 rounded-xl bg-base-100 col-span-2",
            children=[
                html.H3(
                    id="esstential-pie-title",
                    className="text-xl font-medium text-gray-700",
                    children="title",
                ),
                dcc.Graph(id="essentials-chart", figure={}),
            ],
        )

    def _register_callbacks(self):

        @self.app.callback(
            [
                Output("essentials-chart", "figure"),
                Output("esstential-pie-title", "children"),
            ],
            Input("reset-essential-dis", "n_clicks"),
        )
        def handle_reset_click(n_clicks):
            df = self.model.get_essentails_df_whole()
            fig = create_polar_essentails(df)
            title = "Distribution of Essential Service Human Resources Across Administrative Units"
            return fig, title

        @self.app.callback(
            [
                Output("essentials-chart", "figure", allow_duplicate=True),
                Output("esstential-pie-title", "children", allow_duplicate=True),
            ],
            [Input(f"{i}", "n_clicks") for i in self.model.get_list_of_essential_occ()],
            prevent_initial_call=True,
        )
        def hangle_click(*args):
            if ctx.triggered_id:
                df = self.model.get_essential_by_profession(ctx.triggered_id)
                fig = create_essentials_pie(df)

                title = (
                    f"Distribution of {ctx.triggered_id} Across Administrative Units"
                )
            return fig, title
