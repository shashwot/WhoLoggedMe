from sqlalchemy import Boolean, Column, Float, Integer, String, DateTime
from app.core.database import Base
from datetime import datetime


class LogData(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)
    ip_address = Column(String, nullable=False)
    city = Column(String, nullable=True)
    country = Column(String, nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    timezone = Column(String, nullable=True)
    isp = Column(String, nullable=True)
    user_agent = Column(String, nullable=True)
    device_type = Column(String, nullable=True)
    browser = Column(String, nullable=True)
    os = Column(String, nullable=True)
    asn = Column(String, nullable=True)
    is_proxy = Column(Boolean, nullable=True)
    http_method = Column(String, nullable=True)
    request_path = Column(String, nullable=True)
    referrer = Column(String, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
