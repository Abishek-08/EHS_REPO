import os
from dotenv import load_dotenv
from fastapi import FastAPI
from app.models.user import User
from app.models.industry import Industry
from app.models.solution import Solution
from fastapi.middleware.cors import CORSMiddleware
from app.routes.user_router import user_router
from app.routes.industry_router import industry_router
from app.routes.solution_router import solution_router
from app.config import Base, engine

load_dotenv()

# Reading constants from the .env file
version = os.getenv('VERSION')
origins = os.getenv('ORIGINS')

# Initialize the app
app = FastAPI(
    title='EHS-Application',
    version=version,
    description='EHS is a vision AI-based Application',
    root_path=f"{os.getenv('EHS_BASE_URL')}/{version}"
)

# Create the tables using Base.metadata.create_all()
Base.metadata.create_all(engine)  # This will create the tables

# CORS middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(user_router, prefix=f"{os.getenv('USER_ROUTER_BASE_URL')}", tags=['user'])
app.include_router(industry_router,prefix='/industry',tags=['industry'])
app.include_router(solution_router,prefix='/solution',tags=['solution'])