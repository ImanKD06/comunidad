from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# URL de conexión
DATABASE_URL = "mysql+pymysql://root:1307065@localhost:3306/community_manager"
engine = create_engine(DATABASE_URL)

# Crear la sesión
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)