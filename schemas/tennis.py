# Normal way
def recordEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "ATP":item["ATP"],
        "Location":item["Location"],
        "Winner":item["Winner"]
    }

def recordEntity(entity) -> list:
    return [recordEntity(item) for item in entity]
#Best way

def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

def serializeList(entity) -> list:
    return [{a:str(entity[a])} for a in entity]