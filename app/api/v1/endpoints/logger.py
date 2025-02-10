from fastapi import APIRouter, Request
from app.services.ip_service import fetch_ip_details
from app.utils.geoip import get_client_ip, is_proxy

log_router = APIRouter(
    prefix="/log",
    tags=["log"],
)


@log_router.get("/")
async def log_request(request: Request):
    client_ip = get_client_ip(request)
    user_agent = request.headers.get("user-agent")
    http_method = request.method
    request_path = request.url.path
    referrer = request.headers.get("referer")
    is_proxy_detected = is_proxy(request, client_ip)

    fetch_ip_details(
        client_ip,
        user_agent,
        http_method,
        request_path,
        referrer,
        is_proxy_detected,
    )
    return {"message": "Request logged successfully!"}
