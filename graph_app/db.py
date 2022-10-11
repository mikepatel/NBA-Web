"""
Michael Patel
October 2022

Project description:

File description:

"""
################################################################################
# Imports
import pandas as pd
from pymongo import MongoClient

# from other modules in project
import config


################################################################################
def get_data(player_name):
    fields_to_exclude = [
        "_id",
        "Unnamed: 0",
        "Player",
        "player_height",
        "player_weight",
        "college",
        "country",
        "draft_year",
        "draft_round",
        "draft_number",
        "net_rating",
        "oreb_pct",
        "dreb_pct",
        "ast_pct"
    ]
    fields_to_exclude = {field: 0 for field in fields_to_exclude}

    with MongoClient(host=config.MONGO_HOST) as client:
        db = client[config.DATABASE]
        collection = db[config.COLLECTION]

        query = {
            "Player": player_name
        }
        results = collection.find(query, fields_to_exclude)
        results = list(results)

        # convert to dataframe
        df = pd.DataFrame(results)

        # move 'Season' column
        season = df.pop("Season")
        df.insert(0, "Season", season)

        # close connection
        client.close()

        return df
