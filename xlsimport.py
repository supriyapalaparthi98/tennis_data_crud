import csv
import pymongo
import pandas as pd
from config.db import connection
from pymongo import MongoClient

# connection = MongoClient("mongodb://root:pass@localhost:27017/")
print("DB connected")


def main():
    df = pd.read_excel("2011.xls")
    print("reading xls")
    # get the database
    db = connection['tennis_db']

    print("check if collection exists")
    #check if collection exists
    collist = db.list_collection_names()

    if "tennis" in collist:
        print("The collection exists.")
    else:  
        db.create_collection("tennis")

    collection = db.tennis
    #When you try to convert pd.DataFrame to dict, by default to_dict(.) skips the index and only converts the columns.
    #so you set index as a column before use to_dict():

    print("inserting data")
    df.reset_index(level=0, inplace=True)
    collection.insert_many(df.to_dict('records'))
    print("done")


if __name__ == "__main__":
    main()