from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from auth.routes import router as auth_router
from database import engine, Base

# Create the FastAPI instance
app = FastAPI()

# CORS configuration
origins = [
    "http://localhost:3000",  # React frontend
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database tables creation
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Include the authentication routes
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])

# Root route
@app.get("/")
async def root():
    return {"message": "Welcome to the Quiz App!"}
