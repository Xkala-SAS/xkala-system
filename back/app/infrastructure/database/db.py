from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from app.core.settings import settings

from app.infrastructure.database.base.base_class import Base


engine = create_engine(
    settings.DATABASE_URL
)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)