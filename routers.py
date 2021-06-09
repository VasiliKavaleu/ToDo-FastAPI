from fastapi import APIRouter
from user import user_endpoints
from todo_app import todo_endpoints


routes = APIRouter()

routes.include_router(user_endpoints.router, prefix="/user")
routes.include_router(todo_endpoints.router, prefix="/todo")