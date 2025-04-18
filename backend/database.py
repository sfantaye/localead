from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite+aiosqlite:///./test.db"  # Or your actual DB URL

# Create async engine
engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Session maker
async_session_maker = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)

# Declare base
Base = declarative_base()

# This is the missing part!
async def get_async_session() -> AsyncSession:
    async with async_session_maker() as session:
        yield session
