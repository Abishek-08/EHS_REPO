import os
from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

load_dotenv()

# Connect to MongoDB
client = AsyncIOMotorClient(os.getenv('MONGO_DATABASE_URL'))
db = client[os.getenv('MONGO_DATABASE_NAME')]

user_collection = db[os.getenv('MONGO_COLLECTION_USER')]



# Connection to MySQL
engine = create_engine(os.getenv('MYSQL_DATABASE_URL'))

SessionLocal = sessionmaker(bind=engine,autoflush=False,expire_on_commit=False)

connection = engine.connect()

Base = declarative_base()