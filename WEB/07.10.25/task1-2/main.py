from fastapi import HTTPException, FastAPI
from db import SessionLocal
from models import Animal
from tables import AnimalResponse

app = FastAPI()

@app.get("/animals/{animal_id}", response_model=AnimalResponse)
def get_animal(animal_id: int):
    db = SessionLocal()

    animal = db.query(Animal).filter(Animal.id == animal_id).first()

    if not animal:
        raise HTTPException(status_code=404, detail="Тварину не знайдено")

    if animal.age < 0:
        raise HTTPException(status_code=400, detail="Вік не може бути від’ємним")

    return animal