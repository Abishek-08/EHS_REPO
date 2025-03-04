from fastapi import APIRouter,Response
from sqlalchemy.orm import Session
from app.constants.string_constants import STATUS
from app.schemas.industries import Industries
from app.dependency.mysql_dependency import db_dependency
from app.service.industry_service import create_category_service,update_category_service


industry_router = APIRouter()

@industry_router.get('/test')
async def test():
    return {STATUS:"category router is running"}

@industry_router.post('/')
async def create_category(category:Industries,response:Response,db:Session = db_dependency):
    create_category_service(category,db)

@industry_router.put('/')
async def update_category(category:Industries,response:Response,db:Session = db_dependency):
    update_category_service(category,db)
