from fastapi import HTTPException, Request
import geoip2.database
import IP2Proxy
from app.models.logger_model import LogData

GEOIP_CITY_DB_PATH = "./geo/GeoLite2-City.mmdb"
GEOIP_ASN_DB_PATH = "./geo/GeoLite2-ASN.mmdb"
IP2PROXY_DB_PATH = "./geo/IP2PROXY-LITE-PX1.BIN"


def get_client_ip(request: Request) -> str:
    x_forwarded_for = request.headers.get("X-Forwarded-For")
    if x_forwarded_for:
        client_ip = x_forwarded_for.split(",")[0].strip()
    else:
        client_ip = request.client.host

    if not client_ip:
        raise HTTPException(status_code=400, detail="Could not determine client IP")

    return client_ip


def is_proxy(request: Request, ip_address: str) -> bool:
    # proxy_headers = [
    #     "X-Forwarded-For",
    #     "Via",
    #     "Proxy-Connection",
    #     "X-Proxy-ID",
    #     "X-Real-IP",
    # ]
    # for header in proxy_headers:
    #     if header in request.headers:
    #         return True
    proxy_db = IP2Proxy.IP2Proxy()
    proxy_db.open(IP2PROXY_DB_PATH)
    proxy_result = proxy_db.get_all(ip_address)
    return bool(proxy_result["is_proxy"])


def get_ip_details(ip_address: str) -> LogData:
    try:
        with geoip2.database.Reader(GEOIP_CITY_DB_PATH) as city_reader:
            city_response = city_reader.city(ip_address)
            city = city_response.city.name
            country = city_response.country.name
            latitude = city_response.location.latitude
            longitude = city_response.location.longitude
            timezone = city_response.location.time_zone

        with geoip2.database.Reader(GEOIP_ASN_DB_PATH) as asn_reader:
            asn_response = asn_reader.asn(ip_address)
            asn = asn_response.autonomous_system_number
            isp = asn_response.autonomous_system_organization

        return LogData(
            ip_address=ip_address,
            city=city,
            country=country,
            latitude=latitude,
            longitude=longitude,
            timezone=timezone,
            isp=isp,
            asn=asn,
        )
    except Exception as e:
        print(f"Error resolving IP details: {e}")
        return LogData(ip_address=ip_address)
