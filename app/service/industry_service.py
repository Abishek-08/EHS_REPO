from sqlalchemy.orm import Session
from app.schemas.industries import Industries
from app.repository.industry_repo import create_category_repo,update_category_repo

def create_category_service(category:Industries,db:Session):
    create_category_repo(category,db)

def update_category_service(category:Industries,db:Session):
    update_category_repo(category,db)