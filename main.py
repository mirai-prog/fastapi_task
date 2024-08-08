from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("[INFO] The base has been cleared [/INFO]")
    await create_tables()
    print("[INFO] The base is ready for work [/INFO]")
    yield
    print("[INFO] Shutdown [/INFO]")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
