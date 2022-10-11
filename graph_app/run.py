"""
Michael Patel
October 2022

Project description:

File description:

"""
################################################################################
# Imports
from app import app
from layouts import index_layout
import callbacks


# from other modules in project
import config


################################################################################
# Main
if __name__ == "__main__":
    app.title = "NBA Web"
    app.layout = index_layout
    app.run_server(debug=True)
