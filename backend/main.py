from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes.leads import router as leads_router
from backend.database import engine, Base
from backend.routes.auth import router as auth_router
from backend.routes.search_history import router as search_history_router

import asyncio

# Create database tables asynchronously on startup
async def create_database():
    async with engine.begin() as conn:
        # Async create all tables
        await conn.run_sync(Base.metadata.create_all)

app = FastAPI(title="LocaLead API")

origins = [
    "http://localhost",
    "http://localhost:3000",
]

# Add middleware for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def on_startup():
    # Create the database tables during startup
    await create_database()

# Include routes for leads and authentication
app.include_router(leads_router, prefix="/api/leads")
app.include_router(auth_router, prefix="/api/auth")
app.include_router(search_history_router, prefix="/api", tags=["search history"])

