from sqlalchemy.orm import Session,joinedload
from app.models.solution import Solution
from app.schemas.solutions import Solutions

def create_solution_repo(solution:Solutions,db:Session):
    db_solution = Solution(**solution.dict())
    db.add(db_solution)
    db.commit()

def get_solution_by_id_repo(solutionId,db:Session):
    return db.query(Solution).options(joinedload(Solution.industrys)).filter_by(solutionId=solutionId).all()