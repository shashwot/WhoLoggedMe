from app.utils.geoip import get_ip_details
from app.models.logger_model import LogData
from app.core.database import get_db
from datetime import datetime
from user_agents import parse


def fetch_ip_details(
    ip_address: str,
    user_agent: str,
    http_method: str,
    request_path: str,
    referrer: str,
    is_proxy_detected: bool,
) -> LogData:
    log_data = get_ip_details(ip_address)
    log_data.user_agent = user_agent
    log_data.timestamp = datetime.utcnow()
    log_data.http_method = http_method
    log_data.request_path = request_path
    log_data.referrer = referrer
    log_data.is_proxy = is_proxy_detected

    user_agent_parsed = parse(user_agent)
    log_data.device_type = (
        "Mobile"
        if user_agent_parsed.is_mobile
        else "Tablet" if user_agent_parsed.is_tablet else "Desktop"
    )
    log_data.browser = user_agent_parsed.browser.family
    log_data.os = user_agent_parsed.os.family

    db_log = LogData(
        ip_address=log_data.ip_address,
        city=log_data.city,
        country=log_data.country,
        user_agent=log_data.user_agent,
        latitude=log_data.latitude,
        longitude=log_data.longitude,
        timezone=log_data.timezone,
        isp=log_data.isp,
        device_type=log_data.device_type,
        browser=log_data.browser,
        os=log_data.os,
        asn=log_data.asn,
        is_proxy=log_data.is_proxy,
        http_method=log_data.http_method,
        request_path=log_data.request_path,
        referrer=log_data.referrer,
        timestamp=log_data.timestamp,
    )

    db_gen = get_db()
    db = next(db_gen)

    try:
        db.add(db_log)
        db.commit()
        db.refresh(db_log)
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

    return log_data
