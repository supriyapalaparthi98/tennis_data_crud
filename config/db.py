from pymongo import MongoClient

# # for running with docker
connection = MongoClient("mongodb://root:pass@mongo:27017/")


# for local run without docker - run with your own mongo db 
# connection = MongoClient("mongodb://root:pass@localhost:27017/")

