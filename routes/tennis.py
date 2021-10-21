from fastapi import APIRouter
from models.tennis import TennisModel 
from config.db import connection
from schemas.tennis import serializeDict, serializeList
from bson import ObjectId
from bson.json_util import dumps,loads

tennisApp = APIRouter() 

@tennisApp.get('/ping')
async def read_main():
    return {"msg": "Hello World"}


@tennisApp.get('/')
async def find_all_records():
    return serializeList(connection.tennis_db.tennis.find_one())
    # return dumps(connection.tennis_db.tennis.find_one())

@tennisApp.get('/{id}')
async def find_one_record(id):
    return serializeDict(connection.tennis_db.tennis.find_one({"_id":ObjectId(id)}))

@tennisApp.post('/')
async def create_record(record: TennisModel):
    _id =connection.tennis_db.tennis.insert_one(dict(record))
    print(_id.inserted_id )
    # return serializeList(connection.tennis_db.tennis.find_one())
    return serializeList(connection.tennis_db.tennis.find_one({"_id":ObjectId(_id.inserted_id)}))

@tennisApp.put('/{id}')
async def update_record(id,record: TennisModel):
    connection.tennis_db.tennis.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(record)
    })
    return serializeDict(connection.tennis_db.tennis.find_one({"_id":ObjectId(id)}))
    

@tennisApp.delete('/{id}')
async def delete_user(id,record: TennisModel):
    # return serializeDict(connection.tennis_db.tennis.find_one_and_delete({"_id":ObjectId(id)}))
    return dumps(connection.tennis_db.tennis.find_one_and_delete({"_id":ObjectId(id)}))