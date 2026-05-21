from contextlib import asynccontextmanager

from fastapi import HTTPException, FastAPI
import logging

from db import Base, SessionLocal, engine
from models import Task
from tables import TaskResponse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_tables() -> None:
    Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield


app = FastAPI(lifespan=lifespan)

@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    logger.info(f"Запит task_id={task_id}")

    if task_id > 1000:
        logger.error(f"task_id занадто великий: {task_id}")
        raise HTTPException(status_code=422, detail="task_id виходить за межі")

    db = SessionLocal()
    try:
        task = db.query(Task).filter(Task.id == task_id).first()

        if not task:
            logger.error(f"Task не знайдено: {task_id}")
            raise HTTPException(status_code=404, detail="Задачу не знайдено")

        return task
    finally:
        db.close()
