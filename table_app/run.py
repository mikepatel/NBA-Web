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
from fastapi.responses import HTMLResponse, FileResponse
from loguru import logger
import matplotlib.pyplot as plt
import os
import pandas as pd
from pydantic import BaseModel
from pymongo import MongoClient
from typing import Optional

# from other modules in project
import config


################################################################################
# Models
class Player(BaseModel):
    name: str
    seasons: pd.Series
    points: pd.Series

    class Config:
        arbitrary_types_allowed = True


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
    # logger.info(f'{df}')

    p = Player(
        name=f'{first_name} {last_name}',
        seasons=df["Season"],
        points=df["PTS"].astype(float)
    )

    # plot data
    # plt.plot(p.seasons, p.points)
    # filename = "plot.png"
    # filepath = os.path.join(config.TMP_DIR, filename)
    # plt.savefig(filepath)
    return HTMLResponse(content=df.to_html())
    # return FileResponse(filepath)


################################################################################
