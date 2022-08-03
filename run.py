"""
Michael Patel
August 2022

Project description:

File description:

"""
################################################################################
# Imports
from datetime import datetime
from fastapi import FastAPI
from loguru import logger
from pydantic import BaseModel
from pymongo import MongoClient
from typing import Optional

# from other modules in project
from config import *


################################################################################
# Models


################################################################################
# Routes
app = FastAPI()


@app.get("/databases")
async def get_databases():
    with MongoClient(host=HOST) as client:
        return client.list_database_names()


################################################################################
