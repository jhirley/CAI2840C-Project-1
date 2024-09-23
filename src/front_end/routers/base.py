from fastapi import APIRouter
# from src.front_end.routers import route_dashboard
from src.front_end.routers.dashboard import route_dashboard

api_router = APIRouter()
api_router.include_router(route_dashboard.router, prefix="", tags=["Dashboard"])
