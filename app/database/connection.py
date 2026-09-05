import os
import socket
from urllib.parse import urlparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

DATABASE_URL = os.environ.get("DATABASE_URL")

parsed_url = urlparse(DATABASE_URL)
original_host = parsed_url.hostname

try:
    resolved_ip = socket.gethostbyname(original_host)
    db_url_with_ip = DATABASE_URL.replace(original_host, resolved_ip, 1)
except Exception as e:
    print(f"No se pudo resolver la IP en el startup: {e}")
    db_url_with_ip = DATABASE_URL

engine = create_engine(
    db_url_with_ip,
    poolclass=NullPool, 
    connect_args={
        "ssl": {
            "ssl_mode": "REQUIRED",
            "server_hostname": original_host
        },
        "connect_timeout": 10
    }
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()