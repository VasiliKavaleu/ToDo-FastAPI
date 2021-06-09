from fastapi import APIRouter
from user import user_endpoints


routes = APIRouter()

routes.include_router(user_endpoints.router, prefix="/user")
