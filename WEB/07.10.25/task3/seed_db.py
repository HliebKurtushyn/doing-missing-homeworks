from db import SessionLocal, Base, engine
from models import Task

TEST_TASKS = [
    Task(id=1, title="Підготувати звіт", done=False),
    Task(id=2, title="Перевірити API", done=True),
    Task(id=3, title="Оновити документацію", done=False),
    Task(id=4, title="Запустити тести", done=True),
]


def seed_db() -> None:
    Base.metadata.create_all(bind=engine)

    session = SessionLocal()
    try:
        if session.query(Task).count() > 0:
            return

        session.add_all(TEST_TASKS)
        session.commit()
    finally:
        session.close()


if __name__ == "__main__":
    seed_db()
    print("Database seeded successfully.")

