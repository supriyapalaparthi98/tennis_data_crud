from fastapi import FastAPI
from routes.tennis import tennisApp 
from xlsimport import main
app = FastAPI()
app.include_router(tennisApp)
main()


# import uvicorn

# if __name__ == "__main__":
#     uvicorn.run("index:app", host="0.0.0.0", port=8000, reload=True)
   
