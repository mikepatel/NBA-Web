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
from fastapi.responses import HTMLResponse
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
    results = collection.find(query, {"_id": False})
    df = pd.DataFrame(list(results))
    logger.info(f'{df}')
    # return df.to_html()
    return HTMLResponse(content=df.to_html())


################################################################################
