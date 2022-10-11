"""
Michael Patel
October 2022

Project description:

File description:

"""
################################################################################
# Imports
import dash
import dash_bootstrap_components as dbc


################################################################################
app = dash.Dash(
    name=__name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)
