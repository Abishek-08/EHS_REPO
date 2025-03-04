from sqlalchemy.orm import Session,joinedload
from app.dependency.mysql_dependency import db_dependency
from fastapi import APIRouter
from app.constants.string_constants import STATUS
from app.models.solution import Solution
from app.schemas.solutions import Solutions
from app.service.solution_service import create_solution_service,get_solution_by_id_service

solution_router = APIRouter()

@solution_router.get('/test')
async def test():
    return {STATUS:"solution router is running"}

@solution_router.post('/')
async def create_solution(solution:Solutions,db:Session = db_dependency):
     create_solution_service(solution,db)
    

@solution_router.get('/{solutionId}')
async def get_solution_by_industryId(solutionId:int,db:Session = db_dependency):
     return get_solution_by_id_service(solutionId,db)