from fastapi import APIRouter
from user import user_endpoints
from todo_app import todo_endpoints
from tags import tags_endpoints
from asyncdb import endpoints
from app import app_endpoints

routes = APIRouter()

routes.include_router(user_endpoints.router, prefix="/user")
routes.include_router(todo_endpoints.router, prefix="/todo")
routes.include_router(tags_endpoints.router, prefix="/tag")
routes.include_router(endpoints.router, prefix="/asyncdb")
routes.include_router(app_endpoints.router, prefix="/app")
