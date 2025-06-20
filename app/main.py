from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.databases import create_db_and_tables
from app.router.items.router import router as items_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield
    # Cleanup if needed
    print("Shutting down application...")


app = FastAPI(lifespan=lifespan)


@app.get("/", tags=["root"])
def read_root():
    return {"message": "Welcome to the FastAPI application with MySQL!"}


app.include_router(items_router)
