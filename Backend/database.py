from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

# Database URL
DATABASE_URL = "postgresql+asyncpg://postgres:system@localhost:5432/data"


# Create the engine for asyncpg
engine = create_async_engine(DATABASE_URL, echo=True)

# Session factory for database interactions
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# Base class for models
Base = declarative_base()

# Dependency to get a database session
async def get_db():
    async with SessionLocal() as session:
        yield session
