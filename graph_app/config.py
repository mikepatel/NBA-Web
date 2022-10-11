"""
Michael Patel
October 2022

Project description:

File description:

"""
################################################################################
# Imports
import os


################################################################################
# Application
APP_TITLE = "NBA Web"
DEBUG = True

PLAYERS = [
    "LeBron James",
    "Kevin Durant",
    "Stephen Curry",
    "Giannis Antetokounmpo"
]

# Paths
DATA_DIR = os.path.join(os.getcwd(), "data")

# Mongo
MONGO_HOST = "localhost:27017"
DATABASE = "nba"
COLLECTION = "players"
