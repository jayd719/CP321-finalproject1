import dash
from src.model import FifaModel
from src.view import FifaView
from src.controller import FifaController
from src.setup import *
import os


BASE_PATH = os.getenv("DASH_BASE_PATHNAME", "/")

app = dash.Dash(
    __name__,
    external_scripts=JS_SCRIPTS,
    external_stylesheets=SYTLE_SHEETS,
    url_base_pathname=BASE_PATH,
)

# Initialize MVC components
model = FifaModel()
view = FifaView()

# Set the app layout
app.layout = view.layout

FifaController(app, model, view)

application = app.server

if __name__ == "__main__":
    print("HELLO")
    app.run(debug=True)
