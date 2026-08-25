from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker
from app.core.config import settings


# 1. Fetch connection string from environment variables
DATABASE_URL = settings.database_url
# 2. Create Engine with connection health checks
engine = create_engine(
    DATABASE_URL,
    echo=False,  # Set to False in production
    pool_pre_ping=True,  # Automatically recycles stale/broken connections
    pool_size=10,        # Maximum number of permanent connections
    max_overflow=20      # Maximum number of temporary burst connections
)

# 3. Create Session Factory
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


# 4. Declarative Base
class Base(DeclarativeBase):
    pass


# 5. Dependency for FastAPI route handlers
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()