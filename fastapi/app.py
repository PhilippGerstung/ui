from contextlib import asynccontextmanager

import dotenv

from services.scheduler import scheduler

dotenv.load_dotenv()

import uvicorn  # noqa: E402
from fastapi import FastAPI  # noqa: E402

from loguru import logger  # noqa: E402
import schedules  # noqa: E402
from fastapi.middleware.cors import CORSMiddleware # noqa: E402

from routers import prices, recommendations, debug, stations, schedules as schedules_router


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


app = FastAPI(lifespan=lifespan, root_path="/gpv/api")
app.include_router(prices.router)
app.include_router(recommendations.router)
app.include_router(debug.router)
app.include_router(schedules_router.router)
app.include_router(stations.router)


origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def hello_world():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)
