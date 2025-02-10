from fastapi import APIRouter

from app.api.v1.endpoints.logger import log_router as logger_router

routers = APIRouter()
router_list = [
    logger_router,
]

for router in router_list:
    routers.include_router(router)
