from fastapi import APIRouter,Response
from app.schemas.users import Users
from app.constants.string_constants import STATUS
from app.constants.api_constants import LOGIN
from sqlalchemy.orm import Session
from app.dependency.mysql_dependency import db_dependency
from app.service.user_service import register_user_service,login_user_service,get_user_byid_service,get_all_user_service,update_user_service,delete_user_byid_service

user_router = APIRouter()

@user_router.get('/test')
async def test():
    return {STATUS:"user router is running"}

@user_router.post('/')
async def register_user(user: Users, response: Response,db:Session = db_dependency):
    try:
        if register_user_service(user,db):
            response.status_code = 200
            return {STATUS: "user registered successfully"}
        response.status_code = 406
        return {STATUS: "user already present"}
    except Exception as e:
        response.status_code = 500
        return {"error": str(e)}

@user_router.post(LOGIN)
async def login_user(user:Users,response:Response,db:Session = db_dependency):
    try:
        result = login_user_service(user,db)
        if result is not None:
            response.status_code = 200
            return result
        else:
            response.status_code = 404
            return {STATUS:"Invalid user"}
        
    except Exception as e:
        response.status_code = 500
        return {STATUS:e}
    
@user_router.get('/{userId}')
async def get_user_byid(userId:int,response:Response,db:Session = db_dependency):
    try:
        result = get_user_byid_service(userId,db)
        if result is not None:
            response.status_code = 200
            return result
        else:
            response.status_code = 404
            return {STATUS:"user not found"}
        
    except Exception as e:
        response.status_code = 500
        return {STATUS:e}

@user_router.get('/')
async def get_all_user(response:Response,db:Session = db_dependency):
    try:
        result = get_all_user_service(db)
        if result is not None:
            response.status_code = 200
            return result
        response.status_code = 404
        return {STATUS:"userlist not found"}
    except Exception as e:
        response.status_code = 500
        return {STATUS:e}
    
@user_router.put('/')
async def update_user(user:Users,response:Response,db:Session = db_dependency):
    try:
        update_user_service(user,db)
        response.status_code = 200
        return {STATUS:"updation successfully done"}
    except Exception as e:
        response.status_code = 400
        return {STATUS:"updation failure"}
    
@user_router.delete('/{userId}')
async def delete_user_byid(userId:int,response:Response,db:Session = db_dependency):
    try:
        delete_user_byid_service(userId,db)
        response.status_code = 200
        return {STATUS:"deletion successfully done"}
    except Exception as e:
        response.status_code = 500
        return {STATUS:e}

    
