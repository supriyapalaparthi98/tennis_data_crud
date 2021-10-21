
from routes.tennis import tennisApp 
from fastapi.testclient import TestClient

client = TestClient(tennisApp)

jsondata={
                "ATP": "11",
                "Court": "Brisbane International",
                "Date": "02-01-2011",
                "Location": "ATP250",
                "Loser": "Outdoor",
                "Round": "Hard",
                "Series": "1st Round",
                "Surface": "49",
                "Tournament": "Istomin D.",
                "Winner": "De Bakker T."
            }

def test_read_main():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

def test_read_item():
    response = client.get("/")
    assert response.status_code == 200

def test_create_item():
    response = client.post( "/", json=jsondata)
    assert response.status_code == 200
    
   
