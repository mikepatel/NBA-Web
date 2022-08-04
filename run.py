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
import pandas as pd
from pydantic import BaseModel
from pymongo import MongoClient
from typing import Optional

# from other modules in project
import config


################################################################################
# Models


################################################################################
# Setup
app = FastAPI()
client = MongoClient(host=config.HOST)
db = client[config.DATABASE]
collection = db[config.COLLECTION]


################################################################################
# Routes
@app.get("/databases")
async def get_databases():
    return client.list_database_names()


@app.get("/player")
async def get_player(first_name: str, last_name: str):
    query = {
        "Player": f'{first_name} {last_name}'
    }
    results = list(collection.find(query, {"_id": False}))
    logger.info(f'{results}')
    return f'{first_name} {last_name}'


################################################################################
