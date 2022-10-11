"""
Michael Patel
October 2022

Project description:

File description:

"""
################################################################################
# Imports
from dash.dependencies import Input, Output

# from other modules in project
from app import app


################################################################################
@app.callback(
    [
        Output(component_id="player-table", component_property="data"),
        Output(component_id="player-table", component_property="columns")
    ],
    Input(component_id="player-dropdown", component_property="value")
)
def update(value):
    df = get_data(value)
    data = df.to_dict("records")
    columns = [{"name": c, "id": c} for c in df.columns]

    return data, columns
