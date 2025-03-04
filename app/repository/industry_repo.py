from app.schemas.industries import Industries
from app.models.industry import Industry
from sqlalchemy.orm import Session

def create_category_repo(industry:Industries,db:Session):
    db_industry = Industry(**industry.dict())
    db.add(db_industry)
    db.commit()

def update_category_repo(industry:Industries,db:Session):
    db.query(Industry).filter(Industry.industryId == industry.industryId).update(industry.dict())
    db.commit()