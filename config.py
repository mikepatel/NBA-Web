"""
Michael Patel
August 2022

Project description:

File description:

"""
################################################################################
# Imports
import os


################################################################################
# Paths
DATA_DIR = os.path.join(os.getcwd(), "data")
TMP_DIR = os.path.join(DATA_DIR, "tmp")

# Mongo
HOST = "localhost:27017"
DATABASE = "nba"
COLLECTION = "players"
