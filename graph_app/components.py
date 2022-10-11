"""
Michael Patel
October 2022

Project description:

File description:

"""
################################################################################
# Imports
import dash_bootstrap_components as dbc
from dash import dcc
from dash import dash_table

# from other modules in project
import config


################################################################################
# ----- Component: player-dropdown ----- #
players = config.PLAYERS
player_options = [{"label": p, "value": p} for p in players]

player_dropdown = dcc.Dropdown(
    id="player-dropdown",
    options=player_options,
    value=players[0]
)


################################################################################
# ----- Component: player-table ----- #
player_table = dash_table.DataTable(
    id="player-table",
    style_as_list_view=True,
    # style_header={'backgroundColor': 'rgb(30, 30, 30)'},
    # style_cell={
    #     'backgroundColor': 'rgb(50, 50, 50)',
    #     'color': 'white'
    # }
)


################################################################################
# ----- Component: inputs ----- #
inputs = dbc.Container([
    player_dropdown
])


################################################################################
