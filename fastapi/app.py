from contextlib import asynccontextmanager

import dotenv

from routers import recommendations, prices
from services.scheduler import scheduler

dotenv.load_dotenv()

import uvicorn  # noqa: E402
from fastapi import FastAPI  # noqa: E402

from loguru import logger  # noqa: E402
import schedules  # noqa: E402


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Everything runs before startup
    logger.info("Starting scheduler")
    schedules.import_schedules()
    scheduler.start()
    yield
    # Everything runs after shutdown
    logger.info("Stopping scheduler")
    scheduler.shutdown()


app = FastAPI(lifespan=lifespan)
app.include_router(prices.router)
app.include_router(recommendations.router)


@app.get("/")
async def hello_world():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
