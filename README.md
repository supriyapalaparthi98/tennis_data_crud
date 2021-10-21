# Tennis Data Fastapi MongoDB REST API

xlsimport.py : python script to import xls data into mongo db

# Start server : local
makesure Mongodb is up and running
check the connection string in config.db
```
uvicorn index:app --reload

```


# unit tests

```
pytest

```
# Start server : docker
check the connection string in config.db
```
docker-compose up

```

# unit tests

```
docker exec -it <container name> /bin/bash
pytest

```

# api 
goto localhost:8000 to see api response

goto localhost:8000/docs for swagger
