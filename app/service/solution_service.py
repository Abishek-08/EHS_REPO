from sqlalchemy.orm import Session
from app.schemas.solutions import Solutions
from app.repository.solution_repo import create_solution_repo,get_solution_by_id_repo

def create_solution_service(solution:Solutions,db:Session):
    create_solution_repo(solution,db)

def get_solution_by_id_service(solutionId,db:Session):
    return get_solution_by_id_repo(solutionId,db)